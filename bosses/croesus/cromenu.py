import discord
from util import buttons, functions

class CroeMenu(discord.ui.View):
    labels_to_disable = ["Hunter", "Woodcutting", "Mining", "Fishing"]
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

#region hunter button
    @discord.ui.button(label=f"Hunter", style=discord.ButtonStyle.blurple, emoji="🦋", custom_id="crohunt")
    async def hunterbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            hunter_field = embed_dict['fields'][2]['value']
            woodcutting_field = embed_dict['fields'][3]['value']
            mining_field = embed_dict['fields'][4]['value']
            fishing_field = embed_dict['fields'][5]['value']

            if len(functions.get_teamsize(embed)) == 4 and user_mention not in functions.get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in hunter_field:
                new_field = "`Empty`"
            elif hunter_field == "`Empty`" and not any(field == user_mention for field in [woodcutting_field, mining_field, fishing_field]):
                new_field = user_mention
            elif hunter_field != f"`Empty`" and hunter_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🦋 Hunter!", ephemeral=True)
                return
            elif hunter_field == "`Empty`" and any(field == user_mention for field in [woodcutting_field, mining_field, fishing_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return

            embed.set_field_at(2, name=f"🦋 Hunter", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/4")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"hunterbutton error(CroeMenu): {e}")
#endregion

#region woodcutting button
    @discord.ui.button(label=f"Woodcutting", style=discord.ButtonStyle.blurple, emoji="🪓", custom_id="crowood")
    async def woodcuttingbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            hunter_field = embed_dict['fields'][2]['value']
            woodcutting_field = embed_dict['fields'][3]['value']
            mining_field = embed_dict['fields'][4]['value']
            fishing_field = embed_dict['fields'][5]['value']

            if len(functions.get_teamsize(embed)) == 4 and user_mention not in functions.get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in woodcutting_field:
                new_field = "`Empty`"
            elif woodcutting_field == "`Empty`" and not any(field == user_mention for field in [hunter_field, mining_field, fishing_field]):
                new_field = user_mention
            elif woodcutting_field != f"`Empty`" and woodcutting_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🪓 Woodcutting!", ephemeral=True)
                return
            elif woodcutting_field == "`Empty`" and any(field == user_mention for field in [hunter_field, mining_field, fishing_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return

            embed.set_field_at(3, name=f"🪓 Woodcutting", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/4")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"woodcuttingbutton error(CroeMenu): {e}")
#endregion

#region mining button
    @discord.ui.button(label=f"Mining", style=discord.ButtonStyle.blurple, emoji="⛏️", custom_id="cromine")
    async def miningbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            hunter_field = embed_dict['fields'][2]['value']
            woodcutting_field = embed_dict['fields'][3]['value']
            mining_field = embed_dict['fields'][4]['value']
            fishing_field = embed_dict['fields'][5]['value']

            if len(functions.get_teamsize(embed)) == 4 and user_mention not in functions.get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in mining_field:
                new_field = "`Empty`"
            elif mining_field == "`Empty`" and not any(field == user_mention for field in [woodcutting_field, hunter_field, fishing_field]):
                new_field = user_mention
            elif mining_field != f"`Empty`" and mining_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ⛏️ Mining!", ephemeral=True)
                return
            elif mining_field == "`Empty`" and any(field == user_mention for field in [woodcutting_field, hunter_field, fishing_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return

            embed.set_field_at(4, name=f"⛏️ Mining", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/4")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"miningbutton error(CroeMenu): {e}")
#endregion

#region fishing button
    @discord.ui.button(label=f"Fishing", style=discord.ButtonStyle.blurple, emoji="🎣", custom_id="crofish")
    async def fishingbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            hunter_field = embed_dict['fields'][2]['value']
            woodcutting_field = embed_dict['fields'][3]['value']
            mining_field = embed_dict['fields'][4]['value']
            fishing_field = embed_dict['fields'][5]['value']

            if len(functions.get_teamsize(embed)) == 4 and user_mention not in functions.get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in fishing_field:
                new_field = "`Empty`"
            elif fishing_field == "`Empty`" and not any(field == user_mention for field in [woodcutting_field, mining_field, hunter_field]):
                new_field = user_mention
            elif fishing_field != f"`Empty`" and fishing_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🎣 Fishing!", ephemeral=True)
                return
            elif fishing_field == "`Empty`" and any(field == user_mention for field in [woodcutting_field, mining_field, hunter_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return

            embed.set_field_at(5, name=f"🎣 Fishing", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/4")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"fishingbutton error(CroeMenu): {e}")
#endregion

