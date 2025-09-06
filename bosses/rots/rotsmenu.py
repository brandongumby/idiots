import discord
from util import buttons, functions

class RotsMenu(discord.ui.View):
    labels_to_disable = ["Incite West", "DPS West", "Incite East", "DPS East"]
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

#region Incite West button
    @discord.ui.button(label=f"Incite West", style=discord.ButtonStyle.blurple, emoji="↖️", custom_id="rotsiw")
    async def iwestbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            iwest_field = embed_dict['fields'][2]['value']
            dpswest_field = embed_dict['fields'][3]['value']
            ieast_field = embed_dict['fields'][4]['value']
            dpseast_field = embed_dict['fields'][5]['value']


            if len(teamsize) == 4 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif iwest_field == "`Empty`" and not any(field == user_mention for field in [dpswest_field, ieast_field, dpseast_field]):
                embed.set_field_at(2, name=f"↖️ Incite West", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/4")
                await interaction.response.edit_message(embed=embed)

            elif iwest_field == user_mention:
                embed.set_field_at(2, name=f"↖️ Incite West", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/4")
                await interaction.response.edit_message(embed=embed)

            elif iwest_field != f"`Empty`" and iwest_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ↖️ Incite West!", ephemeral=True)

            elif iwest_field == "`Empty`" and any(field == user_mention for field in [dpswest_field, ieast_field, dpseast_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"iwestbutton error(RotsMenu): {e}")
#endregion

#region DPS West button
    @discord.ui.button(label=f"DPS West", style=discord.ButtonStyle.blurple, emoji="↙️", custom_id="rotsdpsw")
    async def dpswestbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            iwest_field = embed_dict['fields'][2]['value']
            dpswest_field = embed_dict['fields'][3]['value']
            ieast_field = embed_dict['fields'][4]['value']
            dpseast_field = embed_dict['fields'][5]['value']


            if len(teamsize) == 4 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif dpswest_field == "`Empty`" and not any(field == user_mention for field in [iwest_field, ieast_field, dpseast_field]):
                embed.set_field_at(3, name=f"↙️ DPS West", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/4")
                await interaction.response.edit_message(embed=embed)

            elif dpswest_field == user_mention:
                embed.set_field_at(3, name=f"↙️ DPS West", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/4")
                await interaction.response.edit_message(embed=embed)

            elif dpswest_field != f"`Empty`" and dpswest_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ↙️ DPS West!", ephemeral=True)

            elif dpswest_field == "`Empty`" and any(field == user_mention for field in [iwest_field, ieast_field, dpseast_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"dpswestbutton error(RotsMenu): {e}")
#endregion

#region incite east button
    @discord.ui.button(label=f"Incite East", style=discord.ButtonStyle.blurple, emoji="↗️", custom_id="rotsie")
    async def ieastbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            iwest_field = embed_dict['fields'][2]['value']
            dpswest_field = embed_dict['fields'][3]['value']
            ieast_field = embed_dict['fields'][4]['value']
            dpseast_field = embed_dict['fields'][5]['value']


            if len(teamsize) == 4 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif ieast_field == "`Empty`" and not any(field == user_mention for field in [iwest_field, dpswest_field, dpseast_field]):
                embed.set_field_at(4, name=f"↗️ Incite East", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/4")
                await interaction.response.edit_message(embed=embed)

            elif ieast_field == user_mention:
                embed.set_field_at(4, name=f"↗️ Incite East", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/4")
                await interaction.response.edit_message(embed=embed)

            elif ieast_field != f"`Empty`" and ieast_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ↗️ Incite East!", ephemeral=True)

            elif ieast_field == "`Empty`" and any(field == user_mention for field in [iwest_field, dpswest_field, dpseast_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"ieastbutton error(RotsMenu): {e}")
#endregion

#region DPS east button
    @discord.ui.button(label=f"DPS East", style=discord.ButtonStyle.blurple, emoji="↘️", custom_id="rotsdpse")
    async def dpseastbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            iwest_field = embed_dict['fields'][2]['value']
            dpswest_field = embed_dict['fields'][3]['value']
            ieast_field = embed_dict['fields'][4]['value']
            dpseast_field = embed_dict['fields'][5]['value']


            if len(teamsize) == 4 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif dpseast_field == "`Empty`" and not any(field == user_mention for field in [iwest_field, dpswest_field, ieast_field]):
                embed.set_field_at(5, name=f"↘️ DPS East", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/4")
                await interaction.response.edit_message(embed=embed)

            elif dpseast_field == user_mention:
                embed.set_field_at(5, name=f"↘️ DPS East", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/4")
                await interaction.response.edit_message(embed=embed)

            elif dpseast_field != f"`Empty`" and dpseast_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ↘️ DPS East!", ephemeral=True)

            elif dpseast_field == "`Empty`" and any(field == user_mention for field in [iwest_field, dpswest_field, ieast_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"dpseastbutton error(RotsMenu): {e}")
#endregion

