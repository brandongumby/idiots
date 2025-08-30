import discord
from util import buttons
from util.functions import get_teamsize

class SolakMenu(discord.ui.View):
    labels_to_disable = ["Base", "North West", "South West", "North East", "South East", "Elf"]
    def __init__(self, client, boss):
            super().__init__(timeout=None)
            self.new_time = None
            self.client = client
            self.is_completed = False
            self.boss = boss
            self.add_item(buttons.CommentButton())
            self.add_item(buttons.PingButton())
            self.add_item(buttons.SetTime())
            self.add_item(buttons.CompleteButton())
            self.add_item(buttons.CloseButton())

#region base button
    @discord.ui.button(label=f"Base", style=discord.ButtonStyle.blurple, emoji="🛡️", custom_id="solakbase")
    async def basebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            elf_field = embed_dict['fields'][7]['value'].split("\n")


            if len(teamsize) == 7 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif base_field == "`Empty`" and not any(field == user_mention for field in elf_field[:2]):
                embed.set_field_at(2, name=f"🛡️ Base", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif base_field == user_mention:
                embed.set_field_at(2, name=f"🛡️ Base", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif base_field != f"`Empty`" and base_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🛡️ Base!", ephemeral=True)

            elif base_field == "`Empty`" and any(field == user_mention for field in elf_field[:2]):
                await interaction.response.send_message(f"You can't be 🧝‍♀️ Elf and 🛡️ Base!", ephemeral=True)
        except Exception as e:
            print(f"basebutton error(SolakMenu): {e}")
#endregion

#region northwest button
    @discord.ui.button(label=f"North West", style=discord.ButtonStyle.blurple, emoji="↖️", custom_id="solaknw")
    async def northwestbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            northwest_field = embed_dict['fields'][3]['value'].split("\n")
            southwest_field = embed_dict['fields'][4]['value'].split("\n")
            northeast_field = embed_dict['fields'][5]['value'].split("\n")
            southeast_field = embed_dict['fields'][6]['value'].split("\n")
            elf_field = embed_dict['fields'][7]['value'].split("\n")


            if len(teamsize) == 7 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            elif (
                "`Empty`" in northwest_field
                and not any(field == user_mention for field in southwest_field[:2])
                and not any(field == user_mention for field in northeast_field[:2])
                and not any(field == user_mention for field in southeast_field[:2])
            ):
                self.add_user(northwest_field, user_mention, user_id)
                combined_value = "\n ".join(northwest_field)
                embed.set_field_at(3, name=f"↖️ North West", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)
                return

            elif user_mention in northwest_field:
                self.remove_user(northwest_field, user_mention, user_id)
                combined_value = "\n ".join(northwest_field)
                embed.set_field_at(3, name=f"↖️ North West", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)
                return

            elif all(field != "`Empty`" for field in northwest_field):
                await interaction.response.send_message(f"↖️ North West role is filled!", ephemeral=True)
                return

            await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"northwestbutton error(SolakMenu): {e}")
#endregion

#region southwest button
    @discord.ui.button(label=f"South West", style=discord.ButtonStyle.blurple, emoji="↙️", custom_id="solaksw")
    async def southwestbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            northwest_field = embed_dict['fields'][3]['value'].split("\n")
            southwest_field = embed_dict['fields'][4]['value'].split("\n")
            northeast_field = embed_dict['fields'][5]['value'].split("\n")
            southeast_field = embed_dict['fields'][6]['value'].split("\n")
            elf_field = embed_dict['fields'][7]['value'].split("\n")


            if len(teamsize) == 7 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            elif (
                "`Empty`" in southwest_field
                and not any(field == user_mention for field in northwest_field[:2])
                and not any(field == user_mention for field in northeast_field[:2])
                and not any(field == user_mention for field in southeast_field[:2])
            ):
                self.add_user(southwest_field, user_mention, user_id)
                combined_value = "\n ".join(southwest_field)
                embed.set_field_at(4, name=f"↙️ South West", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)
                return

            elif user_mention in southwest_field:
                self.remove_user(southwest_field, user_mention, user_id)
                combined_value = "\n ".join(southwest_field)
                embed.set_field_at(4, name=f"↙️ South West", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)
                return

            elif all(field != "`Empty`" for field in southwest_field):
                await interaction.response.send_message(f"↙️ South West role is filled!", ephemeral=True)
                return

            await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"southwestbutton error(SolakMenu): {e}")
#endregion

#region northeast button
    @discord.ui.button(label=f"North East", style=discord.ButtonStyle.blurple, emoji="↗️", custom_id="solakne")
    async def northeastbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            northwest_field = embed_dict['fields'][3]['value'].split("\n")
            southwest_field = embed_dict['fields'][4]['value'].split("\n")
            northeast_field = embed_dict['fields'][5]['value'].split("\n")
            southeast_field = embed_dict['fields'][6]['value'].split("\n")
            elf_field = embed_dict['fields'][7]['value'].split("\n")


            if len(teamsize) == 7 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            elif (
                "`Empty`" in northeast_field
                and not any(field == user_mention for field in northwest_field[:2])
                and not any(field == user_mention for field in southwest_field[:2])
                and not any(field == user_mention for field in southeast_field[:2])
            ):
                self.add_user(northeast_field, user_mention, user_id)
                combined_value = "\n ".join(northeast_field)
                embed.set_field_at(5, name=f"↗️ North East", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)
                return

            elif user_mention in northeast_field:
                self.remove_user(northeast_field, user_mention, user_id)
                combined_value = "\n ".join(northeast_field)
                embed.set_field_at(5, name=f"↗️ North East", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)
                return

            elif all(field != "`Empty`" for field in northeast_field):
                await interaction.response.send_message(f"↗️ North East role is filled!", ephemeral=True)
                return

            await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"northeastbutton error(SolakMenu): {e}")
#endregion

#region southeast button
    @discord.ui.button(label=f"South East", style=discord.ButtonStyle.blurple, emoji="↘️", custom_id="solakse")
    async def southeastbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            northwest_field = embed_dict['fields'][3]['value'].split("\n")
            southwest_field = embed_dict['fields'][4]['value'].split("\n")
            northeast_field = embed_dict['fields'][5]['value'].split("\n")
            southeast_field = embed_dict['fields'][6]['value'].split("\n")
            elf_field = embed_dict['fields'][7]['value'].split("\n")


            if len(teamsize) == 7 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            elif (
                "`Empty`" in southeast_field
                and not any(field == user_mention for field in northwest_field[:2])
                and not any(field == user_mention for field in southwest_field[:2])
                and not any(field == user_mention for field in northeast_field[:2])
            ):
                self.add_user(southeast_field, user_mention, user_id)
                combined_value = "\n ".join(southeast_field)
                embed.set_field_at(6, name=f"↘️ South East", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)
                return

            elif user_mention in southeast_field:
                self.remove_user(southeast_field, user_mention, user_id)
                combined_value = "\n ".join(southeast_field)
                embed.set_field_at(6, name=f"↘️ South East", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)
                return

            elif all(field != "`Empty`" for field in southeast_field):
                await interaction.response.send_message(f"↘️ South East role is filled!", ephemeral=True)
                return

            await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"southeastbutton error(SolakMenu): {e}")
#endregion

#region elf button
    @discord.ui.button(label=f"Elf", style=discord.ButtonStyle.blurple, emoji="🧝‍♀️", custom_id="solakelf")
    async def elfbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            northwest_field = embed_dict['fields'][3]['value'].split("\n")
            southwest_field = embed_dict['fields'][4]['value'].split("\n")
            northeast_field = embed_dict['fields'][5]['value'].split("\n")
            southeast_field = embed_dict['fields'][6]['value'].split("\n")
            elf_field = embed_dict['fields'][7]['value'].split("\n")


            if len(teamsize) == 7 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            if user_mention in elf_field:
                self.remove_user(elf_field, user_mention, user_id)
                combined_value = "\n ".join(elf_field)
                embed.set_field_at(7, name="🧝‍♀️ Elf", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)
                return

            if any(user_mention in field for field in [base_field]):
                await interaction.response.send_message("You can't sign up as 🧝‍♀️ Elf if you've signed up as 🛡️ Base already!", ephemeral=True)
                return

            if all(field != "`Empty`" for field in elf_field):
                await interaction.response.send_message("There is no more room for 🧝‍♀️ Elf", ephemeral=True)
                return

            self.add_user(elf_field, user_mention, user_id)
            combined_value = "\n".join(elf_field)
            embed.set_field_at(7, name="🧝‍♀️ Elf", value=combined_value, inline=True)
            teamsize = get_teamsize(embed)
            embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"elfbutton error(SolakMenu): {e}")

    def remove_user(self, field, user_mention, user_id):
        for i in range(len(field)):
            if field[i] == user_mention:
                field[i] = "`Empty`"
                break

    def add_user(self, field, user_mention, user_id):
        for i in range(len(field)):
            if field[i] == "`Empty`":
                field[i] = user_mention
                break


#endregion

