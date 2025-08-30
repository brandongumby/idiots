import discord
from util import buttons
from util.functions import get_teamsize


class KeraMenu(discord.ui.View):
    labels_to_disable = ["North Echo", "West Echo", "South Echo"]
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

#region north echo button
    @discord.ui.button(label=f"North Echo", style=discord.ButtonStyle.blurple, emoji="⬆️", custom_id="kerane")
    async def northbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            north_field = embed_dict['fields'][2]['value']
            west_field = embed_dict['fields'][3]['value']
            south_field = embed_dict['fields'][4]['value']


            if len(teamsize) == 3 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif north_field == "`Empty`" and not any(field == user_mention for field in [west_field, south_field]):
                embed.set_field_at(2, name=f"⬆️ North Echo", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/3")
                await interaction.response.edit_message(embed=embed)

            elif north_field == user_mention:
                embed.set_field_at(2, name=f"⬆️ North Echo", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/3")
                await interaction.response.edit_message(embed=embed)

            elif north_field != f"`Empty`" and north_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ⬆️ North Echo!", ephemeral=True)

            elif north_field == "`Empty`" and any(field == user_mention for field in [west_field, south_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"northbutton error(KeraMenu): {e}")

#endregion

#region west echo button
    @discord.ui.button(label=f"West Echo", style=discord.ButtonStyle.blurple, emoji="⬅️", custom_id="kerawe")
    async def westbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            north_field = embed_dict['fields'][2]['value']
            west_field = embed_dict['fields'][3]['value']
            south_field = embed_dict['fields'][4]['value']


            if len(teamsize) == 3 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif west_field == "`Empty`" and not any(field == user_mention for field in [north_field, south_field]):
                embed.set_field_at(3, name=f"⬅️ West Echo", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/3")
                await interaction.response.edit_message(embed=embed)

            elif west_field == user_mention:
                embed.set_field_at(3, name=f"⬅️ West Echo", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/3")
                await interaction.response.edit_message(embed=embed)

            elif west_field != f"`Empty`" and west_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ⬅️ West Echo!", ephemeral=True)

            elif west_field == "`Empty`" and any(field == user_mention for field in [north_field, south_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"westbutton error(KeraMenu): {e}")
#endregion

#region south echo button
    @discord.ui.button(label=f"South Echo", style=discord.ButtonStyle.blurple, emoji="⬇️", custom_id="kerase")
    async def southbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            north_field = embed_dict['fields'][2]['value']
            west_field = embed_dict['fields'][3]['value']
            south_field = embed_dict['fields'][4]['value']


            if len(teamsize) == 3 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif south_field == "`Empty`" and not any(field == user_mention for field in [north_field, west_field]):
                embed.set_field_at(4, name=f"⬇️ South Echo", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/3")
                await interaction.response.edit_message(embed=embed)

            elif south_field == user_mention:
                embed.set_field_at(4, name=f"⬇️ South Echo", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/3")
                await interaction.response.edit_message(embed=embed)

            elif south_field != f"`Empty`" and south_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ⬇️ South Echo!", ephemeral=True)

            elif south_field == "`Empty`" and any(field == user_mention for field in [north_field, west_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"southbutton error(KeraMenu): {e}")
#endregion
