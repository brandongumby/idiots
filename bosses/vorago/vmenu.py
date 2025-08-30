import discord
from util import buttons
from util.functions import get_teamsize


class VoragoMenu(discord.ui.View):
    labels_to_disable = ["Base", "Bomb", "TL5", "DPS"]
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
    @discord.ui.button(label=f"Base", style=discord.ButtonStyle.blurple, emoji="🛡️", custom_id="vbase")
    async def basebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            bomb_field = embed_dict['fields'][3]['value']
            tl5_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif base_field == "`Empty`" and not any(field == user_mention for field in dps_field[:2]) and not any(field == user_mention for field in [tl5_field, bomb_field]):
                embed.set_field_at(2, name=f"🛡️ Base Tank", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif base_field == user_mention:
                embed.set_field_at(2, name=f"🛡️ Base Tank", value=f"`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)  

            elif base_field != f"`Empty`" and base_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🛡️ Base Tank!", ephemeral=True)

            elif base_field == "`Empty`" and any(field == user_mention for field in dps_field[:2]) or any(field == user_mention for field in [tl5_field, bomb_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
             print(f"basebutton error(VoragoMenu): {e}")
#endregion

#region bomb button
    @discord.ui.button(label="Bomb", style=discord.ButtonStyle.blurple, emoji="💣", custom_id="vbomb")
    async def bombbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            bomb_field = embed_dict['fields'][3]['value']
            tl5_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif bomb_field == "`Empty`" and not any(field == user_mention for field in dps_field[:2]) and not any(field == user_mention for field in [base_field, tl5_field]):
                embed.set_field_at(3, name="💣 Bomb Tank", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif bomb_field == user_mention:
                embed.set_field_at(3, name="💣 Bomb Tank", value=f"`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed) 

            elif bomb_field != f"`Empty`" and bomb_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 💣 Bomb Tank!", ephemeral=True)

            elif bomb_field == f"`Empty`" and any(field == user_mention for field in dps_field[:2]) or any(field == user_mention for field in [base_field, tl5_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
             print(f"bombbutton error(VoragoMenu): {e}")
#endregion

#region tl5 button
    @discord.ui.button(label="TL5", style=discord.ButtonStyle.blurple, emoji="5️⃣", custom_id="vtl5")
    async def tl5button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            bomb_field = embed_dict['fields'][3]['value']
            tl5_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif tl5_field == f"`Empty`" and base_field != user_mention and bomb_field != user_mention and dps_field[0] != user_mention and dps_field[1] != user_mention:
                embed.set_field_at(4, name="5️⃣ TL5", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif tl5_field == user_mention:
                embed.set_field_at(4, name="5️⃣ TL5", value=f"`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)   

            elif tl5_field != f"`Empty`" and tl5_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 5️⃣ TL5!", ephemeral=True)

            elif tl5_field == f"`Empty`" and base_field == user_mention or bomb_field == user_mention or dps_field[0] == user_mention or dps_field[1] == user_mention:
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
             print(f"tl5button error(VoragoMenu): {e}")
#endregion

#region dps button
    @discord.ui.button(label="DPS", style=discord.ButtonStyle.blurple, emoji="⚔️", custom_id="vdps")
    async def dpsbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            bomb_field = embed_dict['fields'][3]['value']
            tl5_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif dps_field[0] == user_mention:
                dps_field[0] = f"`Empty`"

                combined_value = ", ".join(dps_field)
                embed.set_field_at(5, name="⚔️ DPS", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)   

            elif dps_field[1] == user_mention:
                dps_field[1] = f"`Empty`"
                
                combined_value = ", ".join(dps_field)
                embed.set_field_at(5, name="⚔️ DPS", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif dps_field[0] == f"`Empty`" and dps_field[1] != user_mention and not any(field == user_mention for field in [base_field, bomb_field, tl5_field]):
                dps_field[0] = user_mention

                combined_value = ", ".join(dps_field)
                embed.set_field_at(5, name="⚔️ DPS", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)

            elif dps_field[1] == f"`Empty`" and dps_field[0] != user_mention and not any(field == user_mention for field in [base_field, bomb_field, tl5_field]):
                dps_field[1] = user_mention

                combined_value = ", ".join(dps_field)
                embed.set_field_at(5, name="⚔️ DPS", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/5")
                await interaction.response.edit_message(embed=embed)     

            elif dps_field[0] != f"`Empty`" and dps_field[1] != f"`Empty`":
                await interaction.response.send_message(f"There is no more room for ⚔️ DPS", ephemeral=True)

            elif any(field == f"`Empty`" for field in dps_field[:2]) and any(field == user_mention for field in [base_field, bomb_field, tl5_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
             print(f"dpsbutton error(VoragoMenu): {e}")
#endregion

