import discord
from util import buttons
from util.functions import get_teamsize


class AodMenu(discord.ui.View):
    labels_to_disable = ["Base", "Umbra", "Glacies", "Cruor", "Fumus", "Hammer", "Smoke Cloud"]
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
    @discord.ui.button(label=f"Base", style=discord.ButtonStyle.blurple, emoji="🛡️", custom_id="aodbase")
    async def basebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']
            field_list = [umbra_field, glacies_field, cruor_field, fumus_field, hammer_field, sc_field]
                
            if len(get_teamsize(embed)) == 7 and user_mention not in get_teamsize(embed):
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
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/7")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"basebutton error(AodMenu): {e}")
#endregion

#region umbra button
    @discord.ui.button(label=f"Umbra", style=discord.ButtonStyle.blurple, emoji="🇺", custom_id="aodumbra")
    async def umbrabutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']
            field_list = [base_field, glacies_field, cruor_field, fumus_field, hammer_field, sc_field]

            if len(get_teamsize(embed)) == 7 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            
            if umbra_field == user_mention:
                new_field = "`Empty`"
            elif umbra_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif umbra_field != f"`Empty`" and umbra_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇺 Umbra!", ephemeral=True)
                return
            elif umbra_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return

            embed.set_field_at(3, name=f"🇺 Umbra", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/7")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"umbrabutton error(AodMenu): {e}")
#endregion

#region glacies button
    @discord.ui.button(label=f"Glacies", style=discord.ButtonStyle.blurple, emoji="🇬", custom_id="aodglacies")
    async def glaciesbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']
            field_list = [base_field, umbra_field, cruor_field, fumus_field, hammer_field, sc_field]

            if len(get_teamsize(embed)) == 7 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            
            if glacies_field == user_mention:
                new_field = "`Empty`"
            elif glacies_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif glacies_field != f"`Empty`" and glacies_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇬 Glacies!", ephemeral=True)
                return
            elif glacies_field == "`Empty`" and any(field == user_mention for field in [base_field, umbra_field, cruor_field, fumus_field, hammer_field, sc_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return

            embed.set_field_at(4, name=f"🇬 Glacies", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/7")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"glaciesbutton error(AodMenu): {e}")
#endregion

#region cruor button
    @discord.ui.button(label=f"Cruor", style=discord.ButtonStyle.blurple, emoji="🇨", custom_id="aodcruor")
    async def cruorbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']
            field_list = [base_field, umbra_field, glacies_field, fumus_field, hammer_field, sc_field]

            if len(get_teamsize(embed)) == 7 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            
            if cruor_field == user_mention:
                new_field = "`Empty`"
            elif cruor_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif cruor_field != f"`Empty`" and cruor_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇨 Cruor!", ephemeral=True)
                return
            elif cruor_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return

            embed.set_field_at(5, name=f"🇨 Cruor", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/7")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"cruorbutton error(AodMenu): {e}")
#endregion

#region fumus button
    @discord.ui.button(label=f"Fumus", style=discord.ButtonStyle.blurple, emoji="🇫", custom_id="aodfumus")
    async def fumusbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']
            field_list = [base_field, umbra_field, glacies_field, cruor_field, hammer_field, sc_field]

            if len(get_teamsize(embed)) == 7 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            
            if fumus_field == user_mention:
                new_field = "`Empty`"
            elif fumus_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif fumus_field != f"`Empty`" and fumus_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇫 Fumus!", ephemeral=True)
                return
            elif fumus_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return

            embed.set_field_at(6, name=f"🇫 Fumus", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/7")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"fumusbutton error(AodMenu): {e}")
#endregion

#region hammer button
    @discord.ui.button(label=f"Hammer", style=discord.ButtonStyle.blurple, emoji="🔨", custom_id="aodhammer")
    async def hammerbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']
            field_list = [base_field, umbra_field, glacies_field, cruor_field, fumus_field, sc_field]

            if len(get_teamsize(embed)) == 7 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            
            if hammer_field == user_mention:
                new_field = "`Empty`"
            elif hammer_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif hammer_field != f"`Empty`" and hammer_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🔨 Hammer!", ephemeral=True)
                return
            elif hammer_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
                return

            embed.set_field_at(7, name=f"🔨 Hammer", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/7")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"hammerbutton error(AodMenu): {e}")
#endregion

#region smokecloud button
    @discord.ui.button(label=f"Smoke Cloud", style=discord.ButtonStyle.blurple, emoji="☁️", custom_id="aodsc")
    async def scbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']
            field_list = [base_field, umbra_field, glacies_field, cruor_field, fumus_field, hammer_field]

            if len(get_teamsize(embed)) == 7 and user_mention not in get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            
            if sc_field == user_mention:
                new_field = "`Empty`"
            elif sc_field == "`Empty`" and not any(field == user_mention for field in field_list):
                new_field = user_mention
            elif sc_field != f"`Empty`" and sc_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ☁️ Smoke Cloud!", ephemeral=True)
                return
            elif sc_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)

            embed.set_field_at(8, name=f"☁️ Smoke Cloud", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/7")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"scbutton error(AodMenu): {e}")
#endregion

