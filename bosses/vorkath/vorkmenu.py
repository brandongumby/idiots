import discord
from util import buttons, functions


class VorkMenu(discord.ui.View):
    labels_to_disable = ["Zemo Tank", "Vorky Tank", "DPS"]
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

#region zemo button
    @discord.ui.button(label=f"Zemo Tank", style=discord.ButtonStyle.blurple, emoji="🛡️", custom_id="zemotank")
    async def zemobutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            zemo_field = embed_dict['fields'][2]['value']
            vork_field = embed_dict['fields'][3]['value']
            dps_field = embed_dict['fields'][4]['value'].split(", ")


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif zemo_field == "`Empty`" and not any(field == user_mention for field in dps_field[:8]) and vork_field != user_mention:
                embed.set_field_at(2, name=f"🛡️ Zemo Tank", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif zemo_field == user_mention:
                embed.set_field_at(2, name=f"🛡️ Zemo Tank", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)  

            elif zemo_field != f"`Empty`" and zemo_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🛡️ Zemo Tank!", ephemeral=True)

            elif zemo_field == "`Empty`" and any(field == user_mention for field in dps_field[:8]) or vork_field == user_mention:
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"zemobutton error(VorkMenu): {e}")
#endregion

#region vorky button
    @discord.ui.button(label=f"Vorky Tank", style=discord.ButtonStyle.blurple, emoji="🐲", custom_id="vorktank")
    async def vorkbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            zemo_field = embed_dict['fields'][2]['value']
            vork_field = embed_dict['fields'][3]['value']
            dps_field = embed_dict['fields'][4]['value'].split(", ")


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif vork_field == "`Empty`" and not any(field == user_mention for field in dps_field[:8]) and zemo_field != user_mention:
                embed.set_field_at(3, name=f"🐲 Vorky Tank", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif vork_field == user_mention:
                embed.set_field_at(3, name=f"🐲 Vorky Tank", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)  

            elif vork_field != f"`Empty`" and vork_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🐲 Vorky Tank!", ephemeral=True)

            elif vork_field == "`Empty`" and any(field == user_mention for field in dps_field[:8]) or zemo_field == user_mention:
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"vorkbutton error(VorkMenu): {e}")
#endregion

#region dps button
    @discord.ui.button(label="DPS", style=discord.ButtonStyle.blurple, emoji="⚔️", custom_id="vorkdps")
    async def dpsbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            zemo_field = embed_dict['fields'][2]['value']
            vork_field = embed_dict['fields'][3]['value']
            dps_field = embed_dict['fields'][4]['value'].split(", ")


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message("Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in dps_field:
                self.remove_user(dps_field, user_mention, user_id)
                combined_value = ", ".join(dps_field)
                embed.set_field_at(4, name="⚔️ DPS", value=combined_value, inline=False)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)
                return

            if any(user_mention in field for field in [zemo_field, vork_field]):
                await interaction.response.send_message("You don't need to sign up as ⚔️ DPS if you've signed up as a role already!", ephemeral=True)
                return

            if all(field != "`Empty`" for field in dps_field):
                await interaction.response.send_message("There is no more room for ⚔️ DPS", ephemeral=True)
                return

            self.add_user(dps_field, user_mention, user_id)
            combined_value = ", ".join(dps_field)
            embed.set_field_at(4, name="⚔️ DPS", value=combined_value, inline=False)
            teamsize = functions.get_teamsize(embed)
            embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"dpsbutton error(VorkMenu): {e}")

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

