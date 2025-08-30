import discord
from util import buttons
from util.functions import get_teamsize


class Aod5Menu(discord.ui.View):
    labels_to_disable = ["Base", "Umbra/Glacies", "Cruor/Fumus", "Hammer", "Smoke Cloud"]
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
    @discord.ui.button(label=f"Base", style=discord.ButtonStyle.blurple, emoji="🛡️", custom_id="aod5base")
    async def basebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_glacies_field = embed_dict['fields'][3]['value']
            cruor_fumus_field = embed_dict['fields'][4]['value']
            hammer_field = embed_dict['fields'][5]['value']
            sc_field = embed_dict['fields'][6]['value']
            field_list = [umbra_glacies_field, cruor_fumus_field, hammer_field, sc_field]


            if len(get_teamsize(embed)) == 5 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            elif base_field == user_mention:
                new_field = "`Empty`"
            elif base_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif base_field != f"`Empty`" and base_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🛡️ Base Tank!", ephemeral=True)
                return
            elif base_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return
            
            embed.set_field_at(2, name=f"🛡️ Base Tank", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"basebutton error(Aod5Menu): {e}")
#endregion

#region Umbra/Glacies button
    @discord.ui.button(label=f"Umbra/Glacies", style=discord.ButtonStyle.blurple, emoji="🇺", custom_id="aodumbra_glacies")
    async def aodumbra_glacies(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_glacies_field = embed_dict['fields'][3]['value']
            cruor_fumus_field = embed_dict['fields'][4]['value']
            hammer_field = embed_dict['fields'][5]['value']
            sc_field = embed_dict['fields'][6]['value']
            field_list = [base_field, cruor_fumus_field, hammer_field, sc_field]

            if len(get_teamsize(embed)) == 5 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            elif umbra_glacies_field == user_mention:
                new_field = "`Empty`"
            elif umbra_glacies_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif umbra_glacies_field != f"`Empty`" and umbra_glacies_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇺 Umbra/Glacies!", ephemeral=True)
                return
            elif umbra_glacies_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return
            
            embed.set_field_at(3, name=f"🇺 Umbra/Glacies", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"aodumbra_glacies error(Aod5Menu): {e}")
#endregion

#region Cruor/Fumus button
    @discord.ui.button(label=f"Cruor/Fumus", style=discord.ButtonStyle.blurple, emoji="🇨", custom_id="aodcruor_fumus")
    async def aodcruor_fumus(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_glacies_field = embed_dict['fields'][3]['value']
            cruor_fumus_field = embed_dict['fields'][4]['value']
            hammer_field = embed_dict['fields'][5]['value']
            sc_field = embed_dict['fields'][6]['value']
            field_list = [base_field, umbra_glacies_field, hammer_field, sc_field]

            if len(get_teamsize(embed)) == 5 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            elif cruor_fumus_field == user_mention:
                new_field = "`Empty`"
            elif cruor_fumus_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif cruor_fumus_field != f"`Empty`" and cruor_fumus_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇨 Cruor/Fumus!", ephemeral=True)
                return
            elif cruor_fumus_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return
            
            embed.set_field_at(4, name=f"🇨 Cruor/Fumus", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"aodcruor_fumus error(Aod5Menu): {e}")
#endregion

#region hammer button
    @discord.ui.button(label=f"Hammer", style=discord.ButtonStyle.blurple, emoji="🔨", custom_id="aod5hammer")
    async def hammerbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_glacies_field = embed_dict['fields'][3]['value']
            cruor_fumus_field = embed_dict['fields'][4]['value']
            hammer_field = embed_dict['fields'][5]['value']
            sc_field = embed_dict['fields'][6]['value']
            field_list = [base_field, umbra_glacies_field, cruor_fumus_field, sc_field]

            if len(get_teamsize(embed)) == 5 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            elif hammer_field == user_mention:
                new_field = "`Empty`"
            elif hammer_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif hammer_field != f"`Empty`" and hammer_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🔨 Hammer!", ephemeral=True)
                return
            elif hammer_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return
            
            embed.set_field_at(5, name=f"🔨 Hammer", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"hammerbutton error(Aod5Menu): {e}")
#endregion

#region smokecloud button
    @discord.ui.button(label=f"Smoke Cloud", style=discord.ButtonStyle.blurple, emoji="☁️", custom_id="aod5sc")
    async def scbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_glacies_field = embed_dict['fields'][3]['value']
            cruor_fumus_field = embed_dict['fields'][4]['value']
            hammer_field = embed_dict['fields'][5]['value']
            sc_field = embed_dict['fields'][6]['value']
            field_list = [base_field, umbra_glacies_field, cruor_fumus_field, hammer_field]

            if len(get_teamsize(embed)) == 5 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            elif sc_field == user_mention:
                new_field = "`Empty`"
            elif sc_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif sc_field != f"`Empty`" and sc_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ☁️ Smoke Cloud!", ephemeral=True)
                return
            elif sc_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return
            
            embed.set_field_at(6, name=f"☁️ Smoke Cloud", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"scbutton error(Aod5Menu): {e}")
#endregion

