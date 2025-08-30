import discord
from util import buttons
from util.functions import get_teamsize


class HMVoragoMenu(discord.ui.View):
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
    @discord.ui.button(label=f"Base", style=discord.ButtonStyle.blurple, emoji="🛡️", custom_id="hmvbase")
    async def basebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            bomb_field = embed_dict['fields'][3]['value'].split("\n")
            tl5_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 9 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif base_field == f"`Empty`" and not any(field == user_mention for field in bomb_field[:2]) and not any(field == user_mention for field in dps_field[:5]) and tl5_field != user_mention:
                embed.set_field_at(2, name=f"🛡️ Base Tank", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
                await interaction.response.edit_message(embed=embed)
            elif base_field == user_mention:
                embed.set_field_at(2, name=f"🛡️ Base Tank", value=f"`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
                await interaction.response.edit_message(embed=embed)            
            elif base_field != f"`Empty`" and base_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🛡️ Base Tank!", ephemeral=True)
            elif base_field == f"`Empty`" and any(field == user_mention for field in bomb_field[:2]) or any(field == user_mention for field in dps_field[:5]) or tl5_field == user_mention:
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"basebutton error(HMVoragoMenu): {e}")
#endregion

#region bomb button
    @discord.ui.button(label="Bomb", style=discord.ButtonStyle.blurple, emoji="💣", custom_id="hmvbomb")
    async def bombbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            bomb_field = embed_dict['fields'][3]['value'].split("\n")
            tl5_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 9 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif bomb_field[0] == user_mention:
                bomb_field[0] = "`Empty`"
                combined_value = "\n".join(bomb_field)

                embed.set_field_at(3, name="💣 Bomb Tank", value=combined_value, inline=True)
                
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
                await interaction.response.edit_message(embed=embed)
            elif bomb_field[1] == user_mention:
                bomb_field[1] = "`Empty`"
                combined_value = "\n".join(bomb_field)

                embed.set_field_at(3, name="💣 Bomb Tank", value=combined_value, inline=True)
                
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
                await interaction.response.edit_message(embed=embed) 

            elif bomb_field[0] == f"`Empty`" and bomb_field[1] != user_mention and not any(field == user_mention for field in dps_field[:5]) and not any(field == user_mention for field in [tl5_field, base_field]):
                bomb_field[0] = user_mention

                combined_value = "\n".join(bomb_field)

                embed.set_field_at(3, name="💣 Bomb Tank", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
                await interaction.response.edit_message(embed=embed)

            elif bomb_field[1] == f"`Empty`" and bomb_field[0] != user_mention and not any(field == user_mention for field in dps_field[:5]) and not any(field == user_mention for field in [tl5_field, base_field]):
                bomb_field[1] = user_mention

                combined_value = "\n".join(bomb_field)

                embed.set_field_at(3, name="💣 Bomb Tank", value=combined_value, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
                await interaction.response.edit_message(embed=embed)
            
            elif bomb_field[0] != f"`Empty`" and bomb_field[1] != f"`Empty`":
                await interaction.response.send_message(f"Someone else has signed up as 💣 Bomb Tank!", ephemeral=True)
            elif any(field == user_mention for field in dps_field[:5]) or any(field == user_mention for field in [tl5_field, base_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"bombbutton error(HMVoragoMenu): {e}")
#endregion

#region tl5 button
    @discord.ui.button(label="TL5", style=discord.ButtonStyle.blurple, emoji="5️⃣", custom_id="hmvtl5")
    async def tl5button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            bomb_field = embed_dict['fields'][3]['value'].split("\n")
            tl5_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 9 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif tl5_field == f"`Empty`" and not any(field == user_mention for field in bomb_field[:2]) and not any(field == user_mention for field in dps_field[:5]) and base_field != user_mention:
                embed.set_field_at(4, name="5️⃣ TL5", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
                await interaction.response.edit_message(embed=embed)
            elif tl5_field == user_mention:
                embed.set_field_at(4, name="5️⃣ TL5", value=f"`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
                await interaction.response.edit_message(embed=embed)            
            elif tl5_field != f"`Empty`" and tl5_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 5️⃣ TL5!", ephemeral=True)
            elif tl5_field == f"`Empty`" and any(field == user_mention for field in bomb_field[:2]) or any(field == user_mention for field in dps_field[:5]) or base_field == user_mention:
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"tl5button error(HMVoragoMenu): {e}")
#endregion

#region dps button
    @discord.ui.button(label="DPS", style=discord.ButtonStyle.blurple, emoji="⚔️", custom_id="hmvdps")
    async def dpsbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            bomb_field = embed_dict['fields'][3]['value'].split("\n")
            tl5_field = embed_dict['fields'][4]['value']
            dps_field = embed_dict['fields'][5]['value'].split(", ")


            if len(teamsize) == 9 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            if user_mention in dps_field:
                self.remove_user(dps_field, user_mention, user_id)
                combined_value = ", ".join(dps_field)
                embed.set_field_at(5, name="⚔️ DPS", value=combined_value, inline=False)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
                await interaction.response.edit_message(embed=embed)
                return

            if any(user_mention in field for field in [base_field, tl5_field]) or any(field == user_mention for field in bomb_field[:2]):
                await interaction.response.send_message("You don't need to sign up as ⚔️ DPS if you've signed up as a role already!", ephemeral=True)
                return

            if all(field != "`Empty`" for field in dps_field):
                await interaction.response.send_message("There is no more room for ⚔️ DPS", ephemeral=True)
                return

            self.add_user(dps_field, user_mention, user_id)
            combined_value = ", ".join(dps_field)
            embed.set_field_at(5, name="⚔️ DPS", value=combined_value, inline=False)
            teamsize = get_teamsize(embed)
            embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/9")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"dpsbutton error(HMVoragoMenu): {e}")

    def remove_user(self, dps_field, user_mention, user_id):
        for i in range(len(dps_field)):
            if dps_field[i] == user_mention:
                dps_field[i] = "`Empty`"
                break

    def add_user(self, dps_field, user_mention, user_id):
        for i in range(len(dps_field)):
            if dps_field[i] == "`Empty`":
                dps_field[i] = user_mention
                break
#endregion
