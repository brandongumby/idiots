#region  imports
# Standard library
import time
import random
import calendar
from datetime import datetime, timezone

# Third-party libraries
import discord
from discord import TextStyle
from discord.ui import Modal, TextInput
import pytz
import humanfriendly


# custom modules
from util import myviews, config, functions

#endregion



#region  TimeInputModal
class TimeInputModal(Modal):
    def __init__(self, author_name, client, boss):
        super().__init__(title="Set Event Time")
        self.author_name = author_name
        self.result = None
        self.client = client
        self.boss = boss

        self.add_item(TextInput(label="Date if not today and Time (YYYY-MM-DD HH:MM)", placeholder="2025-07-22 18:30", custom_id="time"))
        self.add_item(TextInput(label="Time Zone (ie. EST, CST, PST, BST, IST, CET)", default="Gametime", custom_id="timezone"))

    async def on_submit(self, interaction: discord.Interaction):
        try:
            date_time = self.children[0].value
            time_zone = self.children[1].value

            if len(date_time) == 5:
                current_date = datetime.now().strftime("%Y-%m-%d")
                date_time = current_date + " " + date_time

            if time_zone.lower() == "est":
                time_zone = "us/eastern"
            elif time_zone.lower() == "cst":
                time_zone = "us/central"
            elif time_zone.lower() == "pst":
                time_zone = "us/pacific"
            elif time_zone.lower() == "bst":
                time_zone = "europe/london"
            elif time_zone.lower() == "ist":
                time_zone = "Asia/Kolkata"
            elif time_zone.lower() == "aest":
                time_zone = "Australia/Queensland"
            elif time_zone.lower() == "gametime":
                time_zone = "UTC"
            
            try:    # Parse the input time
                local_time = time.strptime(date_time, '%Y-%m-%d %H:%M')
                    # Create a naive datetime object
                naive_datetime = datetime(*local_time[:6])
                        
                    # Get the local time zone
                local_tz = pytz.timezone(time_zone)
                local_aware_datetime = local_tz.localize(naive_datetime)
                        
                    # Convert local time to UTC
                utc_datetime = local_aware_datetime.astimezone(pytz.utc)
                new_time = calendar.timegm(utc_datetime.timetuple())

                self.result = new_time

                if new_time < int(time.time()):
                    await interaction.response.send_message(f"An error occurred: You cannot set a time in the past!", ephemeral=True)

                embed = interaction.message.embeds[0]
                embed.set_field_at(0, name="⏰ Start Time", value=f"Event scheduled for <t:{new_time}:F>\n<t:{new_time}:R>", inline=False)
                await interaction.message.edit(embed=embed)
                await interaction.response.send_message(f"New time set!", delete_after=3)

                #ping here
                if interaction.guild_id == config.GUILD_ID:
                    await functions.teamform_ping(self.client, interaction.message, interaction, self.boss, new_time)

            except pytz.UnknownTimeZoneError:
                await interaction.response.send_message(f"Invalid time zone: {time_zone}, If this timezone is correct please contact <@224165409278918656> to add", ephemeral=True)
        except Exception as e:
            print(f"TimeInputModal error: {e}")
#endregion

#region  AddUser
class AddUser(discord.ui.Modal):
    def __init__(self, channel):
        super().__init__(title="Add User to ticket", timeout=300)
        self.channel = channel
        self.user = discord.ui.TextInput(
            label="User ID",
            min_length=2,
            max_length=30,
            required=True,
            placeholder="User ID"
        )
        self.add_item(self.user)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        try:
            user = interaction.guild.get_member(int(self.user.value))
            if user is None:
                return await interaction.response.send_message(f"Invalid User ID: Could not find user with that ID")
            overwrite = discord.PermissionOverwrite()
            overwrite.read_messages = True
            await self.channel.set_permissions(user, overwrite=overwrite)
            await interaction.response.send_message(f"{user.mention} has been added to this ticket.")
        except Exception as e:
            print(f"AddUser error: {e}")
#endregion

#region  RemoveUser
class RemoveUser(discord.ui.Modal):
    def __init__(self, channel):
        super().__init__(title="Remove User to ticket", timeout=300)
        self.channel = channel
        self.user = discord.ui.TextInput(
            label="User ID",
            min_length=2,
            max_length=30,
            required=True,
            placeholder="User ID"
        )
        self.add_item(self.user)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        try:
            user = interaction.guild.get_member(int(self.user.value))
            if user is None:
                return await interaction.response.send_message(f"Invalid User ID: Could not find user with that ID")
            overwrite = discord.PermissionOverwrite()
            overwrite.read_messages = False
            await self.channel.set_permissions(user, overwrite=overwrite)
            await interaction.response.send_message(f"{user.mention} has been removed from this ticket.")
        except Exception as e:
            print(f"RemoveUser error: {e}")
#endregion

#region  CommentInputModal
class CommentInputModal(Modal):
    def __init__(self, author_name):
        super().__init__(title="Add Comment", timeout=None)
        self.author_name = author_name

        self.add_item(TextInput(label="Add any addition comments", placeholder="Add any addition comments", custom_id="comment_modal"))

    async def on_submit(self, interaction: discord.Interaction):
        try:
            added_comment = self.children[0].value
            embed = interaction.message.embeds[0]
                    
            embed.set_field_at(1, name="💬 Comments:", value=f"{added_comment}", inline=False)
            await interaction.message.edit(embed=embed)
            await interaction.response.send_message(f"Comment added!", delete_after=3)
        except Exception as e:
            print(f"CommentInputModal error: {e}")
#endregion

#region  DataUpdateModal
class DataUpdateModal(Modal):
    def __init__(self, client, table_name, identifier_data, identifier, column_list):
        super().__init__(title="Update Database", timeout=None)
        self.table_name = table_name
        self.client = client
        self.identifier_data = identifier_data
        self.identifier = identifier

        self.add_item(TextInput(label=f"{column_list}", placeholder="Column name", custom_id="column"))
        self.add_item(TextInput(label="New Data for the column", placeholder="new data", custom_id="new_data"))
        self.add_item(TextInput(label="Type of data [STRING/INTEGER]", placeholder="STRING", custom_id="data_type"))

        async def on_submit(self, interaction: discord.Interaction):
            try:
                column = self.children[0].value
                new_data = self.children[1].value
                data_type = self.children[2].value

                new_type = data_type.lower()
                if new_type == "integer":
                    new_data = int(new_data)
                if new_type == "int":
                    new_data = int(new_data)
                if new_type == "i":
                    new_data = int(new_data)

                async with self.client.db.cursor() as cursor:
                    await cursor.execute(f"UPDATE {self.table_name} SET {column} = ? WHERE {self.identifier} = ? AND guild = ?", (new_data, self.identifier_data, interaction.guild.id))
                    await self.client.db.commit()
                    await interaction.response.send_message(f"{self.table_name} updated: <@{self.identifier_data}> {column} set to {new_data}", ephemeral=True)
            except Exception as e:
                await interaction.response.send_message("one or more fields had incorrect data", ephemeral=True)
                print(f"DataUpdateModal error: {e}")
#endregion

#region  GiveawayModal
class GiveawayModal(Modal):
    def __init__(self, client, TaskClass):
        super().__init__(title="Create a new Giveaway")
        self.client = client
        self.TaskClass = TaskClass

        self.add_item(TextInput(label="Duration", placeholder="ie. 2 days", custom_id="end_time", required=True))
        self.add_item(TextInput(label="Number of Winners", default="1", custom_id="winners", required=True))
        self.add_item(TextInput(label="Prize", placeholder="Enter prize here", custom_id="prize", required=True))
        self.add_item(TextInput(label="Description", placeholder="add a description..", custom_id="description", required=False, style=TextStyle.long))


    async def on_submit(self, interaction: discord.Interaction):
        try:
            end_time = self.children[0].value
            winners = self.children[1].value
            prize = self.children[2].value
            description = self.children[3].value
            added_time = int(humanfriendly.parse_timespan(end_time))
            now_unix = int(datetime.now(timezone.utc).timestamp())
            end_time = now_unix + added_time
            channel = self.client.get_channel(config.GIVEAWAYS)

            embed = discord.Embed(title="🎉 Idiots Giveaway! 🎉", description=f"{description}", color=0x2986cc)
            embed.set_author(name=f"Hosted by: {interaction.user.name}")
            embed.add_field(name=f"", value=f"Prize: **{prize}**", inline=False)
            embed.add_field(name="", value=f"Ends: <t:{end_time}:R> (<t:{end_time}:f>)\nEntries: 0\nWinners: {winners}", inline=False)
            embed.set_thumbnail(url="https://i.imgur.com/tgQRu7a.png")

            message = await channel.send(embed=embed, view=myviews.GiveawayEnter(self.client, self.TaskClass))

            async with self.client.db.cursor() as cursor:
                await cursor.execute("INSERT INTO giveaways (prize, end_time, description, host, finished, winners, message_id) VALUES (?, ?, ?, ?, ?, ?, ?)", (prize, end_time, description, interaction.user.id, "False", winners, message.id,))
                await self.client.db.commit()

            await interaction.response.send_message("Giveaway created!", ephemeral=True)

            await functions.StartTask(self.TaskClass)
        except Exception as e:
            print(f"GiveawayModal error: {e}")
#endregion

#region  guess_demon
class guess_demon(Modal):
    def __init__(self, client, message):
        super().__init__(title="Guess a Demon name")
        self.client = client
        self.message = message

        self.add_item(TextInput(label="What Demon do you think it is?", placeholder="name here..", custom_id="guess_name"))


    async def on_submit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer(ephemeral=True)
            name_guess = self.children[0].value
            channel_id = interaction.channel.id
            demon_list = ["zazruzath", "moz'giden", "gargranog", "zannemoth", "thizruraz", "joz'ganoth", "dezganur"]
            async with self.client.db.cursor() as cursor:
                await cursor.execute("SELECT team, hp, level, name FROM bosses WHERE channel_id = ?", (channel_id,))

                team, hp, level, name = await cursor.fetchone()

                payload = [team, channel_id]

                if name_guess == "Beezlebub":
                    damage = (level * 100)
                    new_hp = (hp - damage)
                    await cursor.execute("UPDATE bosses SET hp = ? WHERE team = ?", (new_hp, team,))
                    await self.client.db.commit()
                    await self.message.delete()
                    await interaction.followup.send(f"You shout the Demons name and interrupt the summoning\nYour teams Demon, {name}, takes damage from the interruption causing a backfire!\nDamage taken: **{damage}**")
                    await functions.send_demon_view(payload, self.client)
                elif name_guess in demon_list:
                    await interaction.followup.send("I'm willing to bet they aren't summoning a Demon they already summoned.", ephemeral=True)
                else:
                    await interaction.followup.send("That is not the correct Demon, your words were ignored.", ephemeral=True)
        except Exception as e:
            print(f"guess_demon error: {e}")
#endregion

#region  DropChance
class DropChance(Modal):
    def __init__(self):
        super().__init__(title="Simulate drop chances")

        self.add_item(TextInput(label="Enter your current killcount", placeholder="100", custom_id="killcount"))
        self.add_item(TextInput(label="Enter pet or item drop rate", placeholder="drop rate", custom_id="droprate"))
        self.add_item(TextInput(label="Enter pet threshold (0 if item)", placeholder="0", custom_id="threshold"))

    async def on_submit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer(ephemeral=True)
            my_kc = self.children[0].value
            dropchance = self.children[1].value
            pet_thresh = self.children[2].value

            if not my_kc.isdigit():
                await interaction.followup.send("You need to enter a number into the current killcount", ephemeral=True)
            elif not dropchance.isdigit():
                await interaction.followup.send("You need to enter a number into the dropchance", ephemeral=True)
            elif not pet_thresh.isdigit():
                await interaction.followup.send("You need to enter a number into the pet threshold", ephemeral=True)
            else:
                my_kc = int(my_kc)
                dropchance = int(dropchance)
                pet_thresh = int(pet_thresh)

                number_of_drops = 10000

                if 20000 <= dropchance <= 50000:
                    number_of_drops = 1000
                elif 50000 < dropchance <= 100000:
                    number_of_drops = 100
                elif 100000 < dropchance < 2000000:
                    number_of_drops = 10
                elif dropchance >= 2000000:
                    number_of_drops = 1
                elif dropchance < 1:
                    dropchance = 1

                if my_kc < 1:
                    my_kc = 1

                if pet_thresh > 10000:
                    pet_thresh = 10000
                elif pet_thresh < 1:
                    pet_thresh = 10000000

                totalkc = []
                highest = 0
                above_mine = 0
                for _ in range(number_of_drops):
                    rolling = True
                    kc = 0
                    droprate = [0]
                    threshold = 0
                    thresh = 0
                    while rolling:
                        roll = random.randint(0,dropchance)
                        kc += 1
                        threshold += 1
                        if threshold > pet_thresh:
                            thresh += 1
                            droprate.append(thresh)
                            threshold = 0
                        if roll in droprate:
                            rolling = False
                            totalkc.append(kc)
                            if kc > highest:
                                highest = kc
                            if kc > my_kc:
                                above_mine += 1

                average = round(sum(totalkc) / len(totalkc))

                percentage = round(100 - ((above_mine / number_of_drops) * 100), 2)

                if pet_thresh == 10000000:
                    pet_thresh = 0

                dropembed = discord.Embed(title=("Drop Stats"), color=discord.Color.random())
                dropembed.add_field(name=f"", value=f"Simulated **{number_of_drops}** drops at **1/{dropchance}** with a threshold of **{pet_thresh}** *(0 for non pet or no threshold pets)*", inline=False)
                dropembed.add_field(name=f"The Average killcount for drop is: **{average}**", value=f"", inline=False)
                dropembed.add_field(name=f"The Highest killcount was: **{highest}**", value=f"", inline=False)
                dropembed.add_field(name=f"**{percentage}%** of people would have gotten the pet/drop by your killcount *({my_kc})*", value=f"", inline=False)

                await interaction.followup.send(embed=dropembed, ephemeral=True)
        except Exception as e:
            print(f"DropChance error: {e}")
#endregion

