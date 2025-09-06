import discord
from util import buttons, functions

class ZammyMenu(discord.ui.View):
    labels_to_disable = ["Base", "Witch", "Pads", "DPS"]
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
    @discord.ui.button(label=f"Base", style=discord.ButtonStyle.blurple, emoji="🛡️", custom_id="zambase")
    async def basebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            witch_field = embed_dict['fields'][3]['value']
            pads_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif base_field == "`Empty`" and not any(field == user_mention for field in dps_field[:3]) and witch_field != user_mention:
                embed.set_field_at(2, name=f"🛡️ Base", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif base_field == user_mention:
                embed.set_field_at(2, name=f"🛡️ Base", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif base_field != f"`Empty`" and base_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🛡️ Base!", ephemeral=True)

            elif base_field == "`Empty`" and any(field == user_mention for field in dps_field[:3]) or witch_field == user_mention:
                await interaction.response.send_message(f"You are signed up as an incompatible role!", ephemeral=True)
        except Exception as e:
            print(f"basebutton error(ZammyMenu): {e}")
#endregion

#region witch button
    @discord.ui.button(label=f"Witch", style=discord.ButtonStyle.blurple, emoji="🧙‍♀️", custom_id="zamwitch")
    async def witchbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            witch_field = embed_dict['fields'][3]['value']
            pads_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif witch_field == "`Empty`" and base_field != user_mention:
                embed.set_field_at(3, name=f"🧙‍♀️ Witch", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif witch_field == user_mention:
                embed.set_field_at(3, name=f"🧙‍♀️ Witch", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif witch_field != f"`Empty`" and witch_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🧙‍♀️ Witch!", ephemeral=True)

            elif witch_field == "`Empty`" and base_field == user_mention:
                await interaction.response.send_message(f"You are signed up as an incompatible role!", ephemeral=True)
        except Exception as e:
            print(f"witchbutton error(ZammyMenu): {e}")
#endregion

#region pads button
    @discord.ui.button(label=f"Pads", style=discord.ButtonStyle.blurple, emoji="⭕", custom_id="zampads")
    async def padsbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            witch_field = embed_dict['fields'][3]['value']
            pads_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif pads_field == "`Empty`":
                embed.set_field_at(4, name=f"⭕ Pads", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif pads_field == user_mention:
                embed.set_field_at(4, name=f"⭕ Pads", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif pads_field != f"`Empty`" and pads_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ⭕ Pads!", ephemeral=True)
        except Exception as e:
            print(f"padsbutton error(ZammyMenu): {e}")
#endregion

#region dps button
    @discord.ui.button(label=f"DPS", style=discord.ButtonStyle.blurple, emoji="⚔️", custom_id="zamdps")
    async def dpsbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            witch_field = embed_dict['fields'][3]['value']
            pads_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            if user_mention in dps_field:
                self.remove_user(dps_field, user_mention)
                combined_value = ", ".join(dps_field)
                embed.set_field_at(5, name="⚔️ DPS", value=combined_value, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)
                return

            if any(user_mention in field for field in [base_field]):
                await interaction.response.send_message("You can't sign up as ⚔️ DPS if you've signed up as 🛡️ Base already!", ephemeral=True)
                return

            if all(field != "`Empty`" for field in dps_field):
                await interaction.response.send_message("There is no more room for ⚔️ DPS", ephemeral=True)
                return

            self.add_user(dps_field, user_mention)
            combined_value = ", ".join(dps_field)
            embed.set_field_at(5, name="⚔️ DPS", value=combined_value, inline=True)
            teamsize = functions.get_teamsize(embed)
            embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"dpsbutton error(ZammyMenu): {e}")

    def remove_user(self, dps_field, user_mention):
        for i in range(len(dps_field)):
            if dps_field[i] == user_mention:
                dps_field[i] = "`Empty`"
                break

    def add_user(self, dps_field, user_mention):
        for i in range(len(dps_field)):
            if dps_field[i] == "`Empty`":
                dps_field[i] = user_mention
                break
#endregion

