import discord
from util import buttons
from util.functions import get_teamsize

class Aod8Menu(discord.ui.View):
    labels_to_disable = ["Base", "Umbra", "Glacies", "Cruor", "Fumus", "Hammer", "Smoke Cloud", "DPS"]
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
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']


            if base_field == "`Empty`" and not any(field == user_mention for field in [umbra_field, glacies_field, cruor_field, fumus_field, hammer_field, sc_field]):
                embed.set_field_at(2, name=f"🛡️ Base Tank", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif base_field == user_mention:
                embed.set_field_at(2, name=f"🛡️ Base Tank", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif base_field != f"`Empty`" and base_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🛡️ Base Tank!", ephemeral=True)

            elif base_field == "`Empty`" and any(field == user_mention for field in [umbra_field, glacies_field, cruor_field, fumus_field, hammer_field, sc_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"basebutton error(Aod8Menu): {e}")
#endregion

#region umbra button
    @discord.ui.button(label=f"Umbra", style=discord.ButtonStyle.blurple, emoji="🇺", custom_id="aodumbra")
    async def umbrabutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']


            if umbra_field == "`Empty`" and not any(field == user_mention for field in [base_field, glacies_field, cruor_field, fumus_field, hammer_field, sc_field]):
                embed.set_field_at(3, name=f"🇺 Umbra", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif umbra_field == user_mention:
                embed.set_field_at(3, name=f"🇺 Umbra", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif umbra_field != f"`Empty`" and umbra_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇺 Umbra!", ephemeral=True)

            elif umbra_field == "`Empty`" and any(field == user_mention for field in [base_field, glacies_field, cruor_field, fumus_field, hammer_field, sc_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"umbrabutton error(Aod8Menu): {e}")
#endregion

#region glacies button
    @discord.ui.button(label=f"Glacies", style=discord.ButtonStyle.blurple, emoji="🇬", custom_id="aodglacies")
    async def glaciesbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']


    
            if glacies_field == "`Empty`" and not any(field == user_mention for field in [base_field, umbra_field, cruor_field, fumus_field, hammer_field, sc_field]):
                embed.set_field_at(4, name=f"🇬 Glacies", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif glacies_field == user_mention:
                embed.set_field_at(4, name=f"🇬 Glacies", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif glacies_field != f"`Empty`" and glacies_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇬 Glacies!", ephemeral=True)

            elif glacies_field == "`Empty`" and any(field == user_mention for field in [base_field, umbra_field, cruor_field, fumus_field, hammer_field, sc_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"glaciesbutton error(Aod8Menu): {e}")
#endregion

#region cruor button
    @discord.ui.button(label=f"Cruor", style=discord.ButtonStyle.blurple, emoji="🇨", custom_id="aodcruor")
    async def cruorbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']


    
            if cruor_field == "`Empty`" and not any(field == user_mention for field in [base_field, umbra_field, glacies_field, fumus_field, hammer_field, sc_field]):
                embed.set_field_at(5, name=f"🇨 Cruor", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif cruor_field == user_mention:
                embed.set_field_at(5, name=f"🇨 Cruor", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif cruor_field != f"`Empty`" and cruor_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇨 Cruor!", ephemeral=True)

            elif cruor_field == "`Empty`" and any(field == user_mention for field in [base_field, umbra_field, glacies_field, fumus_field, hammer_field, sc_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"cruorbutton error(Aod8Menu): {e}")
#endregion

#region fumus button
    @discord.ui.button(label=f"Fumus", style=discord.ButtonStyle.blurple, emoji="🇫", custom_id="aodfumus")
    async def fumusbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            embed_dict = embed.to_dict()
            teamsize = get_teamsize(embed)
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']


        
            if fumus_field == "`Empty`" and not any(field == user_mention for field in [base_field, umbra_field, glacies_field, cruor_field, hammer_field, sc_field]):
                embed.set_field_at(6, name=f"🇫 Fumus", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif fumus_field == user_mention:
                embed.set_field_at(6, name=f"🇫 Fumus", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif fumus_field != f"`Empty`" and fumus_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇫 Fumus!", ephemeral=True)

            elif fumus_field == "`Empty`" and any(field == user_mention for field in [base_field, umbra_field, glacies_field, cruor_field, hammer_field, sc_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"fumusbutton error(Aod8Menu): {e}")
#endregion

#region hammer button
    @discord.ui.button(label=f"Hammer", style=discord.ButtonStyle.blurple, emoji="🔨", custom_id="aodhammer")
    async def hammerbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']


        
            if hammer_field == "`Empty`" and not any(field == user_mention for field in [base_field, umbra_field, glacies_field, cruor_field, fumus_field, sc_field]):
                embed.set_field_at(7, name=f"🔨 Hammer", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif hammer_field == user_mention:
                embed.set_field_at(7, name=f"🔨 Hammer", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif hammer_field != f"`Empty`" and hammer_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🔨 Hammer!", ephemeral=True)

            elif hammer_field == "`Empty`" and any(field == user_mention for field in [base_field, umbra_field, glacies_field, cruor_field, fumus_field, sc_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"hammerbutton error(Aod8Menu): {e}")
#endregion

#region smokecloud button
    @discord.ui.button(label=f"Smoke Cloud", style=discord.ButtonStyle.blurple, emoji="☁️", custom_id="aodsc")
    async def scbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"
            
            message = interaction.message
            embed = message.embeds[0]
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']


        
            if sc_field == "`Empty`" and not any(field == user_mention for field in [base_field, umbra_field, glacies_field, cruor_field, fumus_field, hammer_field]):
                embed.set_field_at(8, name=f"☁️ Smoke Cloud", value=user_mention, inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif sc_field == user_mention:
                embed.set_field_at(8, name=f"☁️ Smoke Cloud", value="`Empty`", inline=True)
                teamsize = get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/7")
                await interaction.response.edit_message(embed=embed)

            elif sc_field != f"`Empty`" and sc_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ☁️ Smoke Cloud!", ephemeral=True)

            elif sc_field == "`Empty`" and any(field == user_mention for field in [base_field, umbra_field, glacies_field, cruor_field, fumus_field, hammer_field]):
                await interaction.response.send_message(f"You are signed up as another role already!", ephemeral=True)
        except Exception as e:
            print(f"scbutton error(Aod8Menu): {e}")
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
            teamsize = get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            umbra_field = embed_dict['fields'][3]['value']
            glacies_field = embed_dict['fields'][4]['value']
            cruor_field = embed_dict['fields'][5]['value']
            fumus_field = embed_dict['fields'][6]['value']
            hammer_field = embed_dict['fields'][7]['value']
            sc_field = embed_dict['fields'][8]['value']
            dps_field = embed_dict['fields'][9]['value'].split(", ")



            if user_mention in dps_field:
                self.remove_user(dps_field, user_mention, user_id)
                combined_value = ", ".join(dps_field)
                embed.set_field_at(9, name="⚔️ DPS", value=combined_value, inline=False)
                await interaction.response.edit_message(embed=embed)
                return

            if any(user_mention in field for field in [base_field, umbra_field, glacies_field, cruor_field, fumus_field, hammer_field, sc_field]):
                await interaction.response.send_message("You don't need to sign up as ⚔️ DPS if you've signed up as a role already!", ephemeral=True)
                return

            if all(field != "`Empty`" for field in dps_field):
                await interaction.response.send_message("There is no more room for ⚔️ DPS", ephemeral=True)
                return

            self.add_user(dps_field, user_mention, user_id)
            combined_value = ", ".join(dps_field)
            embed.set_field_at(9, name="⚔️ DPS", value=combined_value, inline=False)
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"dpsbutton error(Aod8Menu): {e}")

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
