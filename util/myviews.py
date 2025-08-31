import discord
from util import config, functions, modals, selects
import os
import aiohttp
import json


#region  TicketSettings
class TicketSettings(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client

    @discord.ui.button(label="Add Person", style=discord.ButtonStyle.green, custom_id="add_person")
    async def add_person(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(modals.AddUser(interaction.channel))
        await interaction.response.send_message("Person being added...", delete_after=3)
    
    @discord.ui.button(label="Remove Person", style=discord.ButtonStyle.gray, custom_id="remove_person")
    async def remove_person(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(modals.RemoveUser(interaction.channel))
        await interaction.response.send_message("Person being removed...", delete_after=3)

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.red, custom_id="close_ticket")
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            creator_id = int(interaction.channel.topic)
            creator = interaction.guild.get_member(creator_id)
            guild = interaction.guild.id

            messages = await functions.fetch_all_messages(interaction.channel, 100)
            response = ""
            attachments = []

            async with aiohttp.ClientSession() as session:
                for msg in messages:
                    response += f"{msg.author.name}: {msg.content}\n"
                    for attachment in msg.attachments:
                        response += f"{msg.author.name} sent an attachment: {attachment.url}\n"
                        # Download attachment
                        async with session.get(attachment.url) as resp:
                            if resp.status == 200:
                                file_path = f"{attachment.id}_{attachment.filename}"
                                with open(file_path, 'wb') as f:
                                    f.write(await resp.read())
                                attachments.append(file_path)

            # Write the transcript
            with open('transcript.txt', 'w') as f:
                f.write(response)

            transcript_channel = self.client.get_channel(config.TRANSCRIPT_CHANNEL)
            if transcript_channel is None:
                await interaction.response.send_message("Transcript channel not found.", ephemeral=True)
                return

            await interaction.response.send_message("Ticket is being closed...", ephemeral=True)

            async with self.client.db.cursor() as cursor:
                await cursor.execute("UPDATE tickets SET status = ? WHERE user = ? AND guild = ?", ("closed", creator_id, guild,))
                await self.client.db.commit()
                await interaction.channel.delete()

                try:
                    # Send files to the creator
                    with open('transcript.txt', 'rb') as transcript_file:
                        files = [discord.File(transcript_file)] + [discord.File(fp) for fp in attachments]
                        await creator.send(f"Ticket closed successfully! #{creator.display_name}-ticket", files=files)
                    
                    # Send files to the transcript channel
                    with open('transcript.txt', 'rb') as transcript_file:
                        files = [discord.File(transcript_file)] + [discord.File(fp) for fp in attachments]
                        await transcript_channel.send(f"Ticket transcript for {creator.display_name}:", files=files)
                except Exception as e:
                    await interaction.followup.send(f"Failed to send files: {e}", ephemeral=True)
                finally:
                    # Clean up
                    os.remove('transcript.txt')
                    for file_path in attachments:
                        os.remove(file_path)
        except Exception as e:
            print(f"close_ticket error(TicketSettings): {e}")
#endregion

#region  CreateTicket
class CreateTicket(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client

    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.blurple, custom_id="create_ticket")
    async def create_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user = interaction.user.id
            guild = interaction.guild.id
            async with self.client.db.cursor() as cursor:
                await cursor.execute("SELECT status FROM tickets WHERE user = ? AND guild = ?", (user, guild,))
                status = await cursor.fetchone()
                if not status:
                    await cursor.execute("INSERT INTO tickets (user, guild, status) VALUES (?, ?, ?)", (user, guild, "closed",))
                    await self.client.db.commit()
                try:
                    status = status[0]
                except TypeError:
                    status = "closed"
                if status == "open":
                    return await interaction.response.send_message("You already have a ticket open.", ephemeral=True)

                message = await interaction.response.send_message("A Ticket is being created...", delete_after=1)
                overwrites = {
                    interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    interaction.user: discord.PermissionOverwrite(read_messages=True),
                    interaction.guild.get_role(config.ADMIN_ID): discord.PermissionOverwrite(read_messages=True),
                }   
    
                channel = await interaction.guild.create_text_channel(f"{interaction.user.display_name}-ticket", overwrites=overwrites)

                status = "open"
                await cursor.execute("UPDATE tickets SET status = ? WHERE user = ? AND guild = ?", (status, user, guild,))
                await self.client.db.commit()

                await channel.edit(topic=str(user))
                ticketembed = discord.Embed(title=f"Ticket Created", description=f"{interaction.user.mention} created a ticket!\nClick one of the buttons below to change the settings.")
                await channel.send(f"@here", embed=ticketembed, view=TicketSettings(self.client))
        except Exception as e:
            print(f"create_ticket error(CreateTicket): {e}")
#endregion

#region  QotdView
class QotdView(discord.ui.View):
    def __init__(self, client, tagged_answers, correct_answer, difficulty, results=None, answered=None):
        super().__init__(timeout=None)
        self.client = client
        self.correct_answer = correct_answer  
        self.answered = answered or []  
        self.answer_mapping = {}  
        self.difficulty = difficulty
        self.results = results or {
            '🇦': 0,
            '🇧': 0,
            '🇨': 0,
            '🇩': 0,
        }
        labels = ['🇦', '🇧', '🇨', '🇩']
        
        for index, (answer, identifier) in enumerate(tagged_answers):
            button_style = discord.ButtonStyle.blurple 
            custom_id = f"{identifier}_{index}" 
            button = discord.ui.Button(label="", style=button_style, custom_id=custom_id, emoji=labels[index])

            self.answer_mapping[labels[index]] = answer  
            button.callback = self.create_callback(button)
            self.add_item(button)

        results_button = discord.ui.Button(label="Results", style=discord.ButtonStyle.success, emoji="✅", custom_id="qotdresults")
        results_button.callback = self.show_results
        self.add_item(results_button)

    def create_callback(self, button):
        try:
            async def callback(interaction: discord.Interaction):
                await functions.create_acc(self.client, interaction.user.id, interaction.user.display_name, interaction.guild_id)
                async with self.client.db.cursor() as cursor:
                    user = await functions.load_user(self.client, interaction.user.id, interaction.guild_id)
                    if user.id not in self.answered:
                        self.answered.append(user.id)
                        self.results[button.emoji.name] += 1
                        if "correct" in button.custom_id:
                            if self.difficulty == "hard":
                                points = 10
                            elif self.difficulty == "medium":
                                points = 5
                            elif self.difficulty == "easy":
                                points = 3

                            user.qotd.points += points
                            user.qotd.correct += 1
                            user.qotd.total_questions += 1
                            await user.save()
                            await interaction.response.send_message(f"Correct! You gain {points} points for answering an easy question correctly!", ephemeral=True)
                        else:
                            user.qotd.points += 1
                            user.qotd.total_questions += 1
                            await user.save()
                            await interaction.response.send_message(f"Incorrect answer! The correct answer was: **{self.correct_answer}**, you gain 1 point for answering", ephemeral=True)
                        await cursor.execute("UPDATE users SET qotd_points = ? WHERE guild = ? AND user_id = ?", (user.qotd.points, interaction.guild_id, user.id))
                        await cursor.execute("UPDATE qotd SET results = ?, answered = ? WHERE guild = ?", (json.dumps(self.results), json.dumps(self.answered), config.GUILD_ID))
                        await self.client.db.commit()
                        await functions.update_leaderboard(self.client)
                    else:
                            await interaction.response.send_message("You have already answered this question.", ephemeral=True)
            return callback
        except Exception as e:
            print(f"create_callback error(QotdView): {e}")

    async def show_results(self, interaction: discord.Interaction):
        try:
            user_id = interaction.user.id
            if user_id not in self.answered:
                await interaction.response.send_message("You need to select an answer before seeing what others have chosen!", ephemeral=True)
            else:
                results_message = (
                    f"Results:\n\n"
                    f"🇦: {self.results['🇦']} votes    |   🇧: {self.results['🇧']} votes\n\n"
                    f"🇨: {self.results['🇨']} votes    |   🇩: {self.results['🇩']} votes\n\n"
                )
                await interaction.response.send_message(results_message, ephemeral=True)
        except Exception as e:
            print(f"show_results error(QotdView): {e}")
#endregion

#region  POFTicketSettings
class POFTicketSettings(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.red, custom_id="close_ticket")
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            creator_id = int(interaction.channel.topic)
            creator = interaction.guild.get_member(creator_id)
            guild = interaction.guild.id

            messages = await functions.fetch_all_messages(interaction.channel, 100)
            response = ""
            attachments = []

            async with aiohttp.ClientSession() as session:
                for msg in messages:
                    response += f"{msg.author.name}: {msg.content}\n"
                    for attachment in msg.attachments:
                        response += f"{msg.author.name} sent an attachment: {attachment.url}\n"
                        # Download attachment
                        async with session.get(attachment.url) as resp:
                            if resp.status == 200:
                                file_path = f"{attachment.id}_{attachment.filename}"
                                with open(file_path, 'wb') as f:
                                    f.write(await resp.read())
                                attachments.append(file_path)

            # Write the transcript
            with open('transcript.txt', 'w') as f:
                f.write(response)

            transcript_channel = self.client.get_channel(config.TRANSCRIPT_CHANNEL)
            if transcript_channel is None:
                await interaction.response.send_message("Transcript channel not found.", ephemeral=True)
                return

            await interaction.response.send_message("Ticket is being closed...", ephemeral=True)

            async with self.client.db.cursor() as cursor:
                await cursor.execute("UPDATE tickets SET status = ? WHERE user = ? AND guild = ?", ("closed", creator_id, guild,))
                await self.client.db.commit()
                await interaction.channel.delete()

                try:
                    # Send files to the creator
                    with open('transcript.txt', 'rb') as transcript_file:
                        files = [discord.File(transcript_file)] + [discord.File(fp) for fp in attachments]
                        await creator.send(f"Ticket closed successfully! #{creator.display_name}-ticket", files=files)
                    
                    # Send files to the transcript channel
                    with open('transcript.txt', 'rb') as transcript_file:
                        files = [discord.File(transcript_file)] + [discord.File(fp) for fp in attachments]
                        await transcript_channel.send(f"POF Ticket transcript for {creator.display_name}:", files=files)
                except Exception as e:
                    await interaction.followup.send(f"Failed to send files: {e}", ephemeral=True)
                finally:
                    # Clean up
                    os.remove('transcript.txt')
                    for file_path in attachments:
                        os.remove(file_path)
        except Exception as e:
            print(f"close_ticket error(POFTicketSettings): {e}")
#endregion

#region  CreatePOFTicket
class CreatePOFTicket(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client

    @discord.ui.button(label="Check Animal Status", style=discord.ButtonStyle.green, custom_id="pof_status_check")
    async def pof_status_check(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.send_message(view=POFLendView(self.client), ephemeral=True)
        except Exception as e:
            print(f"pof_status_check error(CreatePOFTicket): {e}")

    @discord.ui.button(label="Request Lend / Support", style=discord.ButtonStyle.blurple, custom_id="create_pof_ticket")
    async def create_pof_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user = interaction.user.id
            guild = interaction.guild.id
            async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT status FROM tickets WHERE user = ? AND guild = ?", (user, guild,))
                    status = await cursor.fetchone()
                    if not status:
                        await cursor.execute("INSERT INTO tickets (user, guild, status) VALUES (?, ?, ?)", (user, guild, "closed",))
                        await self.client.db.commit()
                    try:
                        status = status[0]
                    except TypeError:
                        status = "closed"
                    if status == "open":
                        return await interaction.response.send_message("You already have a ticket open.", ephemeral=True)

                    message = await interaction.response.send_message("A Ticket is being created...", delete_after=1)
                    overwrites = {
                        interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        interaction.user: discord.PermissionOverwrite(read_messages=True),
                    }
                                        
                    channel = await interaction.guild.create_text_channel(f"{interaction.user.display_name}-POF-ticket", overwrites=overwrites)

                    status = "open"
                    await cursor.execute("UPDATE tickets SET status = ? WHERE user = ? AND guild = ?", (status, user, guild,))
                    await self.client.db.commit()

                    await channel.edit(topic=str(user))
                    ticketembed = discord.Embed(title=f"POF Ticket Created", description=f"{interaction.user.mention} created a POF ticket!\nClick one of the buttons below to change the settings.")
                    await channel.send(f"<@229017502859001856>", embed=ticketembed, view=POFTicketSettings(self.client))
        except Exception as e:
            print(f"create_pof_ticket error(CreatePOFTicket): {e}")
#endregion

#region  POFLendView (dropdown view)
class POFLendView(discord.ui.View):
    def __init__(self, client):
            super().__init__(timeout=None)
            self.add_item(selects.POFDropdown(client))
#endregion

#region  TeamformView (dropdown view)
class TeamformView(discord.ui.View):
    def __init__(self, client):
            super().__init__(timeout=None)
            self.add_item(selects.TeamformDropdown(client))
#endregion

#region  AchievementView (dropdown view)
class AchievementView(discord.ui.View):
    def __init__(self, client, uncompleted_list, target_user):
            super().__init__(timeout=None)
            self.add_item(selects.AchievementDropdown(client, uncompleted_list, target_user))
#endregion

#region  AchievementViewMulti (dropdown view)
class AchievementViewMulti(discord.ui.View):
    def __init__(self, client, lists_dict, target_user):
            super().__init__(timeout=None)
            self.add_item(selects.AchievementDropdownMulti(client, lists_dict, target_user))
#endregion

#region  CloseMenu
class CloseMenu(discord.ui.View):
    def __init__(self):
            super().__init__(timeout=None)
            self.value = None
            self.is_completed = False

    @discord.ui.button(label="Close", style=discord.ButtonStyle.red, emoji="⛔", custom_id="rulesclose")
    async def closebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            message = interaction.message
            embed = message.embeds[0]
            
            if embed.author.name == f"Hosted by {interaction.user.name}" or interaction.user.guild_permissions.manage_messages:
                confirmation_view = ConfirmationView(interaction)
                await interaction.response.send_message("Are you sure you want to delete this message?", view=confirmation_view, delete_after=3)
            else:
                await interaction.response.send_message("You are not the author of this embed or you don't have permission to close this.", ephemeral=True)
        except Exception as e:
            print(f"closebutton error(CloseMenu): {e}")
#endregion

#region  ConfirmationView
class ConfirmationView(discord.ui.View):
    def __init__(self, interaction: discord.Interaction):
        super().__init__(timeout=30) 
        self.interaction = interaction

    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.danger)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            if interaction.user == self.interaction.user:
                await self.interaction.message.delete()
                await interaction.response.send_message("Message deleted.", delete_after=1)
                self.stop()
            else:
                await interaction.response.send_message("You cannot confirm this action.", ephemeral=True)
        except Exception as e:
            print(f"confirm error(ConfirmationView): {e}")

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.secondary)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            if interaction.user == self.interaction.user:
                await interaction.response.send_message("Action cancelled.", delete_after=1)
                self.stop()
            else:
                await interaction.response.send_message("You cannot cancel this action.", ephemeral=True)
        except Exception as e:
            print(f"cancel error(ConfirmationView): {e}")
#endregion

#region  GiveawayEnter
class GiveawayEnter(discord.ui.View):
    def __init__(self, client, TaskClass):
        super().__init__(timeout=None)
        self.client = client
        self.TaskClass = TaskClass

    @discord.ui.button(label="Enter", style=discord.ButtonStyle.blurple, emoji="🎉", custom_id="enter_giveaway")
    async def enter_giveaway(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            message = interaction.message
            message_id = interaction.message.id
            user_id = interaction.user.id
            embed = message.embeds[0]
            async with self.client.db.cursor() as cursor:
                await cursor.execute("SELECT participants, end_time, winners, host FROM giveaways WHERE message_id = ?", (message_id,))
                row = await cursor.fetchone()
                end_time = row[1]
                winners = row[2]
                host = row[3]
                if row[0] is None:
                    participants_list = []
                else:
                    participants_list = json.loads(row[0])

                if user_id in participants_list:
                    await interaction.response.send_message("You have already entered the giveaway!", ephemeral=True)
                    return
                participants_list.append(user_id)
                participants = json.dumps(participants_list)
                await cursor.execute("UPDATE giveaways SET participants = ? WHERE message_id = ?", (participants, message_id,))
                await self.client.db.commit()

            embed.set_field_at(1, name="", value=f"Ends: <t:{end_time}:R>, <t:{end_time}:F>\nHosted by: <@{host}>\nEntries: {len(participants_list)}\nWinners: {winners}", inline=False)
            await message.edit(embed=embed)
            await interaction.response.send_message("You have entered the giveaway!", ephemeral=True)
        except Exception as e:
            print(f"enter_giveaway error(GiveawayEnter): {e}")


    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red, emoji="⛔", custom_id="giveaway_cancel")
    async def closebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            message = interaction.message
            embed = message.embeds[0]
            user = interaction.user
            payload = [interaction, user, message]
            if embed.author.name == f"Hosted by: {user.name}" or interaction.user.guild_permissions.manage_messages:
                confirmation_view = GiveawayConfirmView(self.client, self.TaskClass, payload)
                await interaction.response.send_message("Are you sure you want to delete this message?", view=confirmation_view, delete_after=3)
            else:
                await interaction.response.send_message("You are not the author of this embed or you don't have permission to close this.", ephemeral=True)
        except Exception as e:
            print(f"closebutton error(GiveawayEnter): {e}")
#endregion

#region  GiveawayEnd
class GiveawayEnd(discord.ui.View):
    def __init__(self, client, TaskClass):
        super().__init__(timeout=None)
        self.client = client
        self.TaskClass = TaskClass

    @discord.ui.button(label="Reroll Giveaway", style=discord.ButtonStyle.blurple, emoji="🎲", custom_id="reroll_giveaway")
    async def reroll_giveaway(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            message_id = interaction.message.id
            user = interaction.user.id
            async with self.client.db.cursor() as cursor:
                await cursor.execute("SELECT host FROM giveaways WHERE message_id = ?", (message_id,))
                host = await cursor.fetchone()
                host = host[0]

                if user == host or interaction.user.guild_permissions.manage_messages:
                    await cursor.execute("UPDATE giveaways SET finished = ? WHERE message_id = ?", ("False", message_id,))
                    await self.client.db.commit()
                    try:
                        await functions.StartTask(self.TaskClass)
                    except Exception as e:
                        print(e)

                    await interaction.response.send_message(f"🎲 Giveaway has been Rerolled")
                else:
                    await interaction.response.send_message("You don't have permission to Reroll this giveaway.", ephemeral=True)
        except Exception as e:
            print(f"reroll_giveaway error(GiveawayEnd): {e}")
#endregion

#region  ConfirmationView --payload = [interaction, user, message]
class GiveawayConfirmView(discord.ui.View):
    def __init__(self, client, TaskClass, payload):
        super().__init__(timeout=30) 
        self.client = client
        self.interaction = payload[0]
        self.user = payload[1]
        self.message = payload[2]
        self.TaskClass = TaskClass


    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.danger)
    async def gconfirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            if interaction.user == self.user:
                try:
                    message_id = self.message.id
                    async with self.client.db.cursor() as cursor:
                        await cursor.execute("DELETE FROM giveaways WHERE message_id = ?", (message_id,))
                        await self.client.db.commit()
                        await interaction.response.send_message("Message deleted.", delete_after=1)
                        self.stop()
                        await self.message.delete()
                        await functions.StartTask(self.TaskClass)
                except Exception as e:
                    print(e)
            else:
                await interaction.response.send_message("You cannot confirm this action.", ephemeral=True)
        except Exception as e:
            print(f"gconfirm error(GiveawayConfirmView): {e}")

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.secondary)
    async def gcancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            if interaction.user == self.user:
                await interaction.response.send_message("Action cancelled.", delete_after=1)
                self.stop()
            else:
                await interaction.response.send_message("You cannot cancel this action.", ephemeral=True)
        except Exception as e:
            print(f"gcancel error(GiveawayConfirmView): {e}")
#endregion

#region  DemonSpotlightConfirm
class DemonSpotlightConfirm(discord.ui.View):
    def __init__(self, client, message, demon_message, tier):
        super().__init__(timeout=30) 
        self.client = client
        self.message = message
        self.demon_message = demon_message
        self.tier = tier
        self.message_url = message.jump_url


    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green, custom_id="spotlight_yes")
    async def spotlight_yes(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.defer(ephemeral=True)
            if interaction.user.guild_permissions.manage_messages:
                tier = self.tier
                spot = True
                await self.demon_message.delete()
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT boss FROM spotlight WHERE guild = ?", (889687198323048518,))
                    boss = await cursor.fetchone()
                    boss = boss[0]

                    one_list = ["Raids", "GWD 2", "Nex", "Kalphite King"]
                    two_list = ["Araxxi", "Arch-Glacor", "Rasial", "Kerapac", "Barrows: Rise of the Six", "Croesus", "Sanctum of Rebirth", "Elite Dungeons", "Gate of Elidinis"]
                    three_list = ["Zuk", "Telos", "Nex: Angel of Death", "Solak", "Vorago", "Zamorak", "Raksha", "Vorkath"]

                    if boss in one_list:
                        spot_mod = 1.5
                    elif boss in two_list:
                        spot_mod = 1.75
                    elif boss in three_list:
                        spot_mod = 2

                    user_id = interaction.user.id
                    message_id = self.message.id
                    user = self.message.author.id
                    username = self.message.author.display_name
                    channel_id = self.message.channel.id
                    if channel_id == config.DEMONLORDS_CHANNEL:
                        await functions.DamageObelisk(self.client, tier, user)
                        await interaction.followup.send(f"Damage Obelisk Sent", ephemeral=True)
                    else:
                        await cursor.execute("SELECT team, stats FROM bosses WHERE channel_id = ?", (channel_id,))
                        team, team_stats = await cursor.fetchone()
                        team_stats = json.loads(team_stats)
                        await cursor.execute("SELECT exhausted, attacks, stats FROM exhaustion WHERE user = ?", (user,))
                        row = await cursor.fetchone()

                        if row is None:
                            user_stats = {
                                "damage": 0, "t1": 0, "t2": 0, "t3": 0, "t4": 0, "t5": 0, "misses": 0, "highest": 0, "total attacks": 0, "spotlight rolls": 0, "hits": 0
                                }
                            stats = json.dumps(user_stats)
                            await cursor.execute("INSERT INTO exhaustion (username, attacks, exhausted, user, stats) VALUES (?, ?, ?, ?, ?)", (username, 0, 0, user, stats,))
                            await self.client.db.commit()
                            exhausted = 0
                            attacks = 0
                        else:
                            exhausted, attacks, stats = row
                            user_stats = json.loads(stats)
                        guild = interaction.guild.id
                        payload = [team, tier, exhausted, guild, spot, spot_mod]
                        #return_payload = [has_hit, demon_message]

                        return_payload = await functions.DamageDemon(self.client, payload, user, self.message_url)
                        has_hit, demon_message, hit = return_payload

                        if has_hit:
                            attacks += 1
                            user_stats['hits'] += 1
                            team_stats['hits'] += 1
                            user_stats['damage'] += hit
                            if hit > user_stats['highest']:
                                user_stats['highest'] = hit
                            if hit > team_stats['highest']:
                                team_stats['highest'] = hit
                        else:
                            user_stats['misses'] += 1
                            team_stats['misses'] += 1
                        if attacks == 2:
                            attacks = 0
                            exhausted += 1
                        if exhausted >= 5:
                            exhausted = 5

                        tier_string = "t" + str(tier)
                        user_stats[tier_string] += 1
                        user_stats['total attacks'] += 1
                        user_stats['spotlight rolls'] += 1
                        team_stats[tier_string] += 1
                        team_stats['total attacks'] += 1
                        team_stats['spotlight rolls'] += 1
                        stats = json.dumps(user_stats)

                        team_stats = json.dumps(team_stats)

                        await cursor.execute("UPDATE exhaustion SET attacks = ?, exhausted = ?, stats = ? WHERE user = ?", (attacks, exhausted, stats, user,))
                        await cursor.execute("UPDATE bosses SET stats = ? WHERE channel_id = ?", (team_stats, channel_id,))
                        await self.client.db.commit()
                    #adds reaction
                    await self.message.add_reaction("✅")

                    #region send to drops
                    drops_channel = self.client.get_channel(config.DROPS_CHANNEL)

                    content = f"Message from {self.message.author.mention} in {self.message.channel.mention}:\n{self.message.content}"
                    await drops_channel.send(content)

                    for attachment in self.message.attachments:
                        await drops_channel.send(file=await attachment.to_file())
                        #endregion
                    await interaction.followup.send("Message sent to the drops channel!", ephemeral=True)
            else:
                await interaction.followup.send("You do not have permission to use this.", ephemeral=True)
        except Exception as e:
            print(f"spotlight_yes error(DemonSpotlightConfirm): {e}")

    @discord.ui.button(label="No", style=discord.ButtonStyle.red, custom_id="spotlight_no")
    async def spotlight_no(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.defer(ephemeral=True)
            if interaction.user.guild_permissions.manage_messages:
                spot = False
                spot_mod = 1
                tier = self.tier
                await self.demon_message.delete()
                async with self.client.db.cursor() as cursor:
                    user_id = interaction.user.id
                    message_id = self.message.id
                    user = self.message.author.id
                    channel_id = self.message.channel.id
                    if channel_id == config.DEMONLORDS_CHANNEL:
                        await functions.DamageObelisk(self.client, tier)
                        await interaction.followup.send(f"Damage Obelisk Sent", ephemeral=True)
                    else:
                        await cursor.execute("SELECT team, stats FROM bosses WHERE channel_id = ?", (channel_id,))
                        team, team_stats = await cursor.fetchone()
                        team_stats = json.loads(team_stats)
                        await cursor.execute("SELECT exhausted, attacks, stats FROM exhaustion WHERE user = ?", (user,))
                        row = await cursor.fetchone()

                        if row is None:
                            user_stats = {
                                "damage": 0, "t1": 0, "t2": 0, "t3": 0, "t4": 0, "t5": 0, "misses": 0, "highest": 0, "total attacks": 0, "spotlight rolls": 0, "hits": 0
                                }
                            stats = json.dumps(user_stats)
                            await cursor.execute("INSERT INTO exhaustion (attacks, exhausted, user, stats) VALUES (?, ?, ?, ?)", (0, 0, user, stats,))
                            exhausted = 0
                            attacks = 0
                        else:
                            exhausted, attacks, stats = row
                            user_stats = json.loads(stats)
                        guild = interaction.guild.id
                        payload = [team, tier, exhausted, guild, spot, spot_mod]

                        #return_payload = [has_hit, demon_message]
                        try:
                            return_payload = await functions.DamageDemon(self.client, payload, user, self.message_url)
                        except Exception as e:
                            print(e)

                        has_hit, demon_message, hit = return_payload

                        if has_hit:
                            attacks += 1
                            user_stats['hits'] += 1
                            team_stats['hits'] += 1
                            user_stats['damage'] += hit
                            if hit > user_stats['highest']:
                                user_stats['highest'] = hit
                            if hit > team_stats['highest']:
                                team_stats['highest'] = hit
                        else:
                            user_stats['misses'] += 1
                            team_stats['misses'] += 1
                        if attacks == 2:
                            attacks = 0
                            exhausted += 1
                        if exhausted >= 5:
                            exhausted = 5

                        tier_string = "t" + str(tier)
                        user_stats[tier_string] += 1
                        user_stats['total attacks'] += 1
                        stats = json.dumps(user_stats)
                        team_stats[tier_string] += 1
                        team_stats['total attacks'] += 1

                        team_stats = json.dumps(team_stats)

                        await cursor.execute("UPDATE exhaustion SET attacks = ?, exhausted = ?, stats = ? WHERE user = ?", (attacks, exhausted, stats, user,))
                        await cursor.execute("UPDATE bosses SET stats = ? WHERE channel_id = ?", (team_stats, channel_id,))
                        await self.client.db.commit()
                    #adds reaction
                    await self.message.add_reaction("✅")

                    #region send to drops
                    drops_channel = self.client.get_channel(config.DROPS_CHANNEL)

                    content = f"Message from {self.message.author.mention} in {self.message.channel.mention}:\n{self.message.content}"
                    await drops_channel.send(content)

                    for attachment in self.message.attachments:
                        await drops_channel.send(file=await attachment.to_file())
                        #endregion
                    await interaction.followup.send("Message sent to the drops channel!", ephemeral=True)
            else:
                await interaction.followup.send("You do not have permission to use this.", ephemeral=True)
        except Exception as e:
            print(f"spotlight_no error(DemonSpotlightConfirm): {e}")
#endregion

#region  RollDamageTier
class RollDamageTier(discord.ui.View):
    def __init__(self, client, message, demon_message):
        super().__init__(timeout=None)
        self.client = client
        self.message = message
        self.demon_message = demon_message

    @discord.ui.button(label="Tier 1", style=discord.ButtonStyle.blurple, emoji="1️⃣", custom_id="t1_demon")
    async def t1_demon(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.defer(ephemeral=True)
            if interaction.user.guild_permissions.manage_messages:
                channel_id = interaction.channel.id
                demon_channel = self.client.get_channel(channel_id)
                await self.demon_message.delete()

                await interaction.followup.send("Tier 1 selected", ephemeral=True)

                view=DemonSpotlightConfirm(self.client, self.message, demon_message=None, tier=1)
                demon_message2 = await demon_channel.send("Is this drop from a boss on spotlight?", view=view)
                view.demon_message = demon_message2
            else:
                await interaction.followup.send("You don't have permission to use that.", ephemeral=True)
        except Exception as e:
            print(f"t1_demon error(RollDamageTier): {e}")

    @discord.ui.button(label="Tier 2", style=discord.ButtonStyle.blurple, emoji="2️⃣", custom_id="t2_demon")
    async def t2_demon(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.defer(ephemeral=True)
            if interaction.user.guild_permissions.manage_messages:
                channel_id = interaction.channel.id
                demon_channel = self.client.get_channel(channel_id)
                await self.demon_message.delete()

                await interaction.followup.send("Tier 2 selected", ephemeral=True)

                view=DemonSpotlightConfirm(self.client, self.message, demon_message=None, tier=2)
                demon_message2 = await demon_channel.send("Is this drop from a boss on spotlight?", view=view)
                view.demon_message = demon_message2
            else:
                await interaction.followup.send("You don't have permission to use that.", ephemeral=True)
        except Exception as e:
            print(f"t2_demon error(RollDamageTier): {e}")

    @discord.ui.button(label="Tier 3", style=discord.ButtonStyle.blurple, emoji="3️⃣", custom_id="t3_demon")
    async def t3_demon(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.defer(ephemeral=True)
            if interaction.user.guild_permissions.manage_messages:
                channel_id = interaction.channel.id
                demon_channel = self.client.get_channel(channel_id)
                await self.demon_message.delete()

                await interaction.followup.send("Tier 3 selected", ephemeral=True)

                view=DemonSpotlightConfirm(self.client, self.message, demon_message=None, tier=3)
                demon_message2 = await demon_channel.send("Is this drop from a boss on spotlight?", view=view)
                view.demon_message = demon_message2
            else:
                await interaction.followup.send("You don't have permission to use that.", ephemeral=True)
        except Exception as e:
            print(f"t3_demon error(RollDamageTier): {e}")

    @discord.ui.button(label="Tier 4", style=discord.ButtonStyle.blurple, emoji="4️⃣", custom_id="t4_demon")
    async def t4_demon(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.defer(ephemeral=True)
            if interaction.user.guild_permissions.manage_messages:
                channel_id = interaction.channel.id
                demon_channel = self.client.get_channel(channel_id)
                await self.demon_message.delete()

                await interaction.followup.send("Tier 4 selected", ephemeral=True)

                view=DemonSpotlightConfirm(self.client, self.message, demon_message=None, tier=4)
                demon_message2 = await demon_channel.send("Is this drop from a boss on spotlight?", view=view)
                view.demon_message = demon_message2
            else:
                await interaction.followup.send("You don't have permission to use that.", ephemeral=True)
        except Exception as e:
            print(f"t4_demon error(RollDamageTier): {e}")

    @discord.ui.button(label="Tier 5", style=discord.ButtonStyle.blurple, emoji="5️⃣", custom_id="t5_demon")
    async def t5_demon(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await interaction.response.defer(ephemeral=True)
            if interaction.user.guild_permissions.manage_messages:
                channel_id = interaction.channel.id
                demon_channel = self.client.get_channel(channel_id)
                await self.demon_message.delete()

                await interaction.followup.send("Tier 5 selected", ephemeral=True)

                view=DemonSpotlightConfirm(self.client, self.message, demon_message=None, tier=5)
                demon_message2 = await demon_channel.send("Is this drop from a boss on spotlight?", view=view)
                view.demon_message = demon_message2 
            else:
                await interaction.followup.send("You don't have permission to use that.", ephemeral=True)
        except Exception as e:
            print(f"t5_demon error(RollDamageTier): {e}")       
#endregion

#region  TriviaView
class TriviaView(discord.ui.View):
    def __init__(self, client, tagged_answers, correct_answer, difficulty):
        super().__init__(timeout=None)
        self.client = client
        self.correct_answer = correct_answer  
        self.answered = []  
        self.answer_mapping = {}  
        self.difficulty = difficulty
        self.results = {
            '🇦': 0,
            '🇧': 0,
            '🇨': 0,
            '🇩': 0,
        }
        labels = ['🇦', '🇧', '🇨', '🇩']
        

        for index, (answer, identifier) in enumerate(tagged_answers):
            button_style = discord.ButtonStyle.blurple 
            custom_id = f"{identifier}_{index}" 
            button = discord.ui.Button(label="", style=button_style, custom_id=custom_id, emoji=labels[index])

            self.answer_mapping[labels[index]] = answer  
            button.callback = self.create_callback(button)
            self.add_item(button)

    def create_callback(self, button):
        try:
            async def callback(interaction: discord.Interaction):
                user_id = interaction.user.id
                username = interaction.user.name
                try:
                    if f'{username}' not in config.triviadict:
                        config.triviadict[f'{username}'] = 0
                except Exception as e:
                    print(e)
                if user_id not in self.answered:
                        self.answered.append(user_id)
                        answer = self.answer_mapping[button.emoji.name]  
                        self.results[button.emoji.name] += 1
                        if "correct" in button.custom_id:
                            await interaction.response.send_message("Correct! You gain 1 point for answering a question correctly!", ephemeral=True)
                            try:
                                config.triviadict[f'{username}'] += 1
                            except Exception as e:
                                print(e)
                        else:
                            await interaction.response.send_message(f"Incorrect answer! The correct answer was: **{self.correct_answer}**", ephemeral=True)
                else:
                        await interaction.response.send_message("You have already answered this question.", ephemeral=True)
            return callback
        except Exception as e:
            print(f"create_callback error(TriviaView): {e}")
#endregion

#region  DropAward menu
class DropAward(discord.ui.View):
    def __init__(self, target_user, message):
            super().__init__(timeout=None)
            self.value = None
            self.target_user = target_user
            self.message = message
            self.usr = target_user.achievements.drops

    @discord.ui.button(label="Low drop (approx. <50m)", style=discord.ButtonStyle.blurple, emoji="⬇️", custom_id="low_drop")
    async def low_drop(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            emoji = interaction.client.get_emoji(config.DROP_EMOJI)
            await self.message.add_reaction(emoji)
            self.usr.logged.append(self.message.id)
            self.usr.points += 3
            await self.target_user.save()
            await interaction.response.edit_message(content="You have awarded a LOW tier drop!", view=None)
        except Exception as e:
            print(f"low_drop error(DropAward): {e}")

    @discord.ui.button(label="Medium drop (approx. 50m-250m)", style=discord.ButtonStyle.blurple, emoji="🔵", custom_id="med_drop")
    async def med_drop(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            emoji = interaction.client.get_emoji(config.DROP_EMOJI)
            await self.message.add_reaction(emoji)
            self.usr.logged.append(self.message.id)
            self.usr.points += 6
            await self.target_user.save()
            await interaction.response.edit_message(content="You have awarded a MEDIUM tier drop!", view=None)
        except Exception as e:
            print(f"med_drop error(DropAward): {e}")

    @discord.ui.button(label="High drop (approx. >250m)", style=discord.ButtonStyle.blurple, emoji="⬆️", custom_id="high_drop")
    async def high_drop(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            emoji = interaction.client.get_emoji(config.DROP_EMOJI)
            await self.message.add_reaction(emoji)
            self.usr.logged.append(self.message.id)
            self.usr.points += 9
            await self.target_user.save()
            await interaction.response.edit_message(content="You have awarded a HIGH tier drop!", view=None)
        except Exception as e:
            print(f"high_drop error(DropAward): {e}")
#endregion

