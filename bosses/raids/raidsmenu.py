import discord
from util import buttons, functions


class RaidsMenu(discord.ui.View):
    labels_to_disable = ["Base", "Backup SC", "Pet Tank 1/3", "Pet Tank 2", "North Chargers", "Main Stun", "Backup Stun", "North Tank", "Poison Tank", "CPR", "Double", "Jelly Wrangler", "Shark 10", "Stun 0", "Stun 5", "DPS"]
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
    @discord.ui.button(label=f"Base", style=discord.ButtonStyle.blurple, emoji="🛡️", custom_id="raidsbase")
    async def basebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            busc_field = embed_dict['fields'][3]['value']
            pt13_field = embed_dict['fields'][4]['value']
            pt2_field = embed_dict['fields'][5]['value']
            northcharge_field = embed_dict['fields'][6]['value']
            northtank_field = embed_dict['fields'][9]['value']
            psntank_field = embed_dict['fields'][10]['value']
            cpr_field = embed_dict['fields'][11]['value']
            double_field = embed_dict['fields'][12]['value']
            jelly_field = embed_dict['fields'][13]['value']
            shark_field = embed_dict['fields'][14]['value']
            stun0_field = embed_dict['fields'][15]['value']
            stun5_field = embed_dict['fields'][16]['value'].split("\n")
            dps_field = embed_dict['fields'][17]['value'].split(", ")

            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif base_field == f"`Empty`" and not any(field == user_mention for field in stun5_field[:2]) and not any(field == user_mention for field in dps_field[:5]) and not any(field == user_mention for field in [busc_field, pt13_field, pt2_field, northcharge_field, northtank_field, psntank_field, cpr_field, double_field, jelly_field, shark_field, stun0_field]):
                embed.set_field_at(2, name=f"🛡️ Base Tank", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif base_field == user_mention:
                embed.set_field_at(2, name=f"🛡️ Base Tank", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed) 

            elif base_field != f"`Empty`" and base_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🛡️ Base Tank!", ephemeral=True)

            elif base_field == f"`Empty`" and any(field == user_mention for field in stun5_field[:2]) or any(field == user_mention for field in dps_field[:5]) or any(field == user_mention for field in [busc_field, pt13_field, pt2_field, northcharge_field, northtank_field, psntank_field, cpr_field, double_field, jelly_field, shark_field, stun0_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"basebutton error(RaidsMenu): {e}")
#endregion

#region backup button
    @discord.ui.button(label=f"Backup SC", style=discord.ButtonStyle.blurple, emoji="🅱️", custom_id="raidsbusc")
    async def buscbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            busc_field = embed_dict['fields'][3]['value']
            pt13_field = embed_dict['fields'][4]['value']
            pt2_field = embed_dict['fields'][5]['value']
            northcharge_field = embed_dict['fields'][6]['value']


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif busc_field == f"`Empty`" and not any(field == user_mention for field in [base_field, pt13_field, pt2_field, northcharge_field]):
                embed.set_field_at(3, name=f"🅱️ Backup SC", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)
            elif busc_field == user_mention:
                embed.set_field_at(3, name=f"🅱️ Backup SC", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)            
            elif busc_field != f"`Empty`" and busc_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🅱️ Backup SC!", ephemeral=True)
            elif busc_field == f"`Empty`" and any(field == user_mention for field in [base_field, pt13_field, pt2_field, northcharge_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"buscbutton error(RaidsMenu): {e}")
#endregion

#region pet tank 1/3 button
    @discord.ui.button(label=f"Pet Tank 1/3", style=discord.ButtonStyle.blurple, emoji="1️⃣", custom_id="raidspt13")
    async def pt13button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            busc_field = embed_dict['fields'][3]['value']
            pt13_field = embed_dict['fields'][4]['value']
            pt2_field = embed_dict['fields'][5]['value']
            northcharge_field = embed_dict['fields'][6]['value']


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif pt13_field == f"`Empty`" and not any(field == user_mention for field in [base_field, busc_field, pt2_field, northcharge_field]):
                embed.set_field_at(4, name=f"1️⃣ Pet Tank 1/3", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)
            elif pt13_field == user_mention:
                embed.set_field_at(4, name=f"1️⃣ Pet Tank 1/3", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)            
            elif pt13_field != f"`Empty`" and pt13_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 1️⃣ Pet Tank 1/3!", ephemeral=True)
            elif pt13_field == f"`Empty`" and any(field == user_mention for field in [base_field, busc_field, pt2_field, northcharge_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"pt13button error(RaidsMenu): {e}")
#endregion

#region pet tank 2 button
    @discord.ui.button(label=f"Pet Tank 2", style=discord.ButtonStyle.blurple, emoji="2️⃣", custom_id="raidspt2")
    async def pt2button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            busc_field = embed_dict['fields'][3]['value']
            pt13_field = embed_dict['fields'][4]['value']
            pt2_field = embed_dict['fields'][5]['value']
            northcharge_field = embed_dict['fields'][6]['value']


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif pt2_field == f"`Empty`" and not any(field == user_mention for field in [base_field, busc_field, pt13_field, northcharge_field]):
                embed.set_field_at(5, name=f"2️⃣ Pet Tank 2", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)
            elif pt2_field == user_mention:
                embed.set_field_at(5, name=f"2️⃣ Pet Tank 2", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)            
            elif pt2_field != f"`Empty`" and pt2_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 2️⃣ Pet Tank 2!", ephemeral=True)
            elif pt2_field == f"`Empty`" and any(field == user_mention for field in [base_field, busc_field, pt13_field, northcharge_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"pt2button error(RaidsMenu): {e}")
#endregion

#region north charger button
    @discord.ui.button(label=f"North Chargers", style=discord.ButtonStyle.blurple, emoji="🐶", custom_id="raidsnc")
    async def ncbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            busc_field = embed_dict['fields'][3]['value']
            pt13_field = embed_dict['fields'][4]['value']
            pt2_field = embed_dict['fields'][5]['value']
            northcharge_field = embed_dict['fields'][6]['value']


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif northcharge_field == f"`Empty`" and not any(field == user_mention for field in [base_field, busc_field, pt13_field, pt2_field]):
                embed.set_field_at(6, name=f"🐶 North Chargers", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)
            elif northcharge_field == user_mention:
                embed.set_field_at(6, name=f"🐶 North Chargers", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)            
            elif northcharge_field != f"`Empty`" and northcharge_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🐶 North Chargers!", ephemeral=True)
            elif northcharge_field == f"`Empty`" and any(field == user_mention for field in [base_field, busc_field, pt13_field, pt2_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"ncbutton error(RaidsMenu): {e}")
#endregion

#region mainstun button
    @discord.ui.button(label=f"Main Stun", style=discord.ButtonStyle.blurple, emoji="💥", custom_id="raidms")
    async def mainstunbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            mainstun_field = embed_dict['fields'][7]['value']
            bustun_field = embed_dict['fields'][8]['value']


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif mainstun_field == f"`Empty`" and bustun_field != user_mention:
                embed.set_field_at(7, name=f"💥 Main Stun", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif mainstun_field == user_mention:
                embed.set_field_at(7, name=f"💥 Main Stun", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed) 

            elif mainstun_field != f"`Empty`" and mainstun_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 💥 Main Stun!", ephemeral=True)

            elif mainstun_field == f"`Empty`" and bustun_field == user_mention:
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"mainstunbutton error(RaidsMenu): {e}")
#endregion

#region backup stun button index 7
    @discord.ui.button(label=f"Backup Stun", style=discord.ButtonStyle.blurple, emoji="⚡", custom_id="raidsbs")
    async def bustunbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            mainstun_field = embed_dict['fields'][7]['value']
            bustun_field = embed_dict['fields'][8]['value']


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif bustun_field == f"`Empty`" and mainstun_field != user_mention:
                embed.set_field_at(8, name=f"⚡ Backup Stun", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif bustun_field == user_mention:
                embed.set_field_at(8, name=f"⚡ Backup Stun", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed) 

            elif bustun_field != f"`Empty`" and bustun_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ⚡ Backup Stun!", ephemeral=True)

            elif bustun_field == f"`Empty`" and mainstun_field == user_mention:
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"bustunbutton error(RaidsMenu): {e}")
#endregion

#region north tank button index 8
    @discord.ui.button(label=f"North Tank", style=discord.ButtonStyle.blurple, emoji="🐍", custom_id="raidsnt")
    async def northtankbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            northtank_field = embed_dict['fields'][9]['value']
            jelly_field = embed_dict['fields'][13]['value']
            shark_field = embed_dict['fields'][14]['value']
            stun0_field = embed_dict['fields'][15]['value']
            stun5_field = embed_dict['fields'][16]['value'].split("\n")
            dps_field = embed_dict['fields'][17]['value'].split(", ")


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif northtank_field == f"`Empty`" and not any(field == user_mention for field in stun5_field[:2]) and not any(field == user_mention for field in [base_field, jelly_field, shark_field, stun0_field]):
                embed.set_field_at(9, name=f"🐍 North Tank", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif northtank_field == user_mention:
                embed.set_field_at(9, name=f"🐍 North Tank", value=f"`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed) 

            elif northtank_field != f"`Empty`" and northtank_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🐍 North Tank!", ephemeral=True)

            elif northtank_field == f"`Empty`" and any(field == user_mention for field in stun5_field[:2]) or any(field == user_mention for field in [base_field, jelly_field, shark_field, stun0_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"northtankbutton error(RaidsMenu): {e}")
#endregion

#region psn tank button index 9
    @discord.ui.button(label=f"Poison Tank", style=discord.ButtonStyle.blurple, emoji="🤢", custom_id="raidspsn")
    async def psntankbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            psntank_field = embed_dict['fields'][10]['value']
            cpr_field = embed_dict['fields'][11]['value']
            double_field = embed_dict['fields'][12]['value']


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif psntank_field == "`Empty`" and not any(field == user_mention for field in [base_field, cpr_field, double_field]):
                embed.set_field_at(10, name=f"🤢 Poison Tank", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif psntank_field == user_mention:
                embed.set_field_at(10, name=f"🤢 Poison Tank", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif psntank_field != "`Empty`" and psntank_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🤢 Poison Tank!", ephemeral=True)

            elif psntank_field == "`Empty`" and any(field == user_mention for field in [base_field, cpr_field, double_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"psntankbutton error(RaidsMenu): {e}") 
#endregion

#region cpr button index 10
    @discord.ui.button(label=f"CPR", style=discord.ButtonStyle.blurple, emoji="❤️", custom_id="raidscpr")
    async def cprtankbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            psntank_field = embed_dict['fields'][10]['value']
            cpr_field = embed_dict['fields'][11]['value']
            double_field = embed_dict['fields'][12]['value']


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif cpr_field == "`Empty`" and not any(field == user_mention for field in [base_field, psntank_field, double_field]):
                embed.set_field_at(11, name=f"❤️ CPR", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif cpr_field == user_mention:
                embed.set_field_at(11, name=f"❤️ CPR", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif cpr_field != "`Empty`" and cpr_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ❤️ CPR!", ephemeral=True)

            elif cpr_field == "`Empty`" and any(field == user_mention for field in [base_field, psntank_field, double_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"cprtankbutton error(RaidsMenu): {e}") 
#endregion

#region double button index 11
    @discord.ui.button(label=f"Double", style=discord.ButtonStyle.blurple, emoji="🇩", custom_id="raidsdbl")
    async def doublebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            psntank_field = embed_dict['fields'][10]['value']
            cpr_field = embed_dict['fields'][11]['value']
            double_field = embed_dict['fields'][12]['value']


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif double_field == "`Empty`" and not any(field == user_mention for field in [base_field, psntank_field, cpr_field]):
                embed.set_field_at(12, name=f"🇩 Double", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif double_field == user_mention:
                embed.set_field_at(12, name=f"🇩 Double", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif double_field != "`Empty`" and double_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🇩 Double!", ephemeral=True)

            elif double_field == "`Empty`" and any(field == user_mention for field in [base_field, psntank_field, cpr_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"doublebutton error(RaidsMenu): {e}") 
#endregion

#region jelly button index 12
    @discord.ui.button(label=f"Jelly Wrangler", style=discord.ButtonStyle.blurple, emoji="🪼", custom_id="raidsjelly")
    async def jellybutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            northtank_field = embed_dict['fields'][9]['value']
            jelly_field = embed_dict['fields'][13]['value']
            shark_field = embed_dict['fields'][14]['value']
            stun0_field = embed_dict['fields'][15]['value']
            stun5_field = embed_dict['fields'][16]['value'].split("\n")


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif jelly_field == "`Empty`" and not any(field == user_mention for field in stun5_field[:2]) and not any(field == user_mention for field in [base_field, northtank_field, shark_field, stun0_field]):
                embed.set_field_at(13, name=f"🪼 Jelly Wrangler", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif jelly_field == user_mention:
                embed.set_field_at(13, name=f"🪼 Jelly Wrangler", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif jelly_field != "`Empty`" and jelly_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🪼 Jelly Wrangler!", ephemeral=True)

            elif jelly_field == "`Empty`" and any(field == user_mention for field in stun5_field[:2]) or any(field == user_mention for field in [base_field, northtank_field, shark_field, stun0_field, stun5_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"jellybutton error(RaidsMenu): {e}") 
#endregion

#region shark10 button index 13
    @discord.ui.button(label=f"Shark 10", style=discord.ButtonStyle.blurple, emoji="🦈", custom_id="raidsshark10")
    async def sharkbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            northtank_field = embed_dict['fields'][9]['value']
            jelly_field = embed_dict['fields'][13]['value']
            shark_field = embed_dict['fields'][14]['value']
            stun0_field = embed_dict['fields'][15]['value']
            stun5_field = embed_dict['fields'][16]['value'].split("\n")


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif shark_field == "`Empty`" and not any(field == user_mention for field in stun5_field[:2]) and not any(field == user_mention for field in [base_field, northtank_field, jelly_field, stun0_field]):
                embed.set_field_at(14, name=f"🦈 Shark 10", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif shark_field == user_mention:
                embed.set_field_at(14, name=f"🦈 Shark 10", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif shark_field != "`Empty`" and shark_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🦈 Shark 10!", ephemeral=True)

            elif shark_field == "`Empty`" and any(field == user_mention for field in stun5_field[:2]) or any(field == user_mention for field in [base_field, northtank_field, jelly_field, stun0_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"sharkbutton error(RaidsMenu): {e}") 
#endregion

#region stun0 button index 14
    @discord.ui.button(label=f"Stun 0", style=discord.ButtonStyle.blurple, emoji="0️⃣", custom_id="raidsstune0")
    async def stun0button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            northtank_field = embed_dict['fields'][9]['value']
            jelly_field = embed_dict['fields'][13]['value']
            shark_field = embed_dict['fields'][14]['value']
            stun0_field = embed_dict['fields'][15]['value']
            stun5_field = embed_dict['fields'][16]['value'].split("\n")


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif stun0_field == "`Empty`" and not any(field == user_mention for field in stun5_field[:2]) and not any(field == user_mention for field in [base_field, northtank_field, jelly_field, shark_field]):
                embed.set_field_at(15, name=f"0️⃣ Stun 0", value=user_mention, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif stun0_field == user_mention:
                embed.set_field_at(15, name=f"0️⃣ Stun 0", value="`Empty`", inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif stun0_field != "`Empty`" and stun0_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 0️⃣ Stun 0!", ephemeral=True)

            elif stun0_field == "`Empty`" and any(field == user_mention for field in stun5_field[:2]) or any(field == user_mention for field in [base_field, northtank_field, jelly_field, shark_field, stun5_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"stun0button error(RaidsMenu): {e}") 
#endregion

#region stun5 button index 15 
    @discord.ui.button(label=f"Stun 5", style=discord.ButtonStyle.blurple, emoji="5️⃣", custom_id="raidsstun5")
    async def stun5button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            northtank_field = embed_dict['fields'][9]['value']
            jelly_field = embed_dict['fields'][13]['value']
            shark_field = embed_dict['fields'][14]['value']
            stun0_field = embed_dict['fields'][15]['value']
            stun5_field = embed_dict['fields'][16]['value'].split("\n")
            dps_field = embed_dict['fields'][17]['value'].split(", ")


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            elif stun5_field[0] == user_mention:
                stun5_field[0] = "`Empty`"
                combined_value = "\n".join(stun5_field)

                embed.set_field_at(16, name="5️⃣ Stun 5", value=combined_value, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif stun5_field[1] == user_mention:
                stun5_field[1] = "`Empty`"
                combined_value = "\n".join(stun5_field)

                embed.set_field_at(16, name="5️⃣ Stun 5", value=combined_value, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif stun5_field[0] == "`Empty`" and stun5_field[1] != user_mention and not any(field == user_mention for field in [stun0_field, shark_field, jelly_field, northtank_field, base_field]):
                stun5_field[0] = user_mention
                combined_value = "\n".join(stun5_field)

                embed.set_field_at(16, name="5️⃣ Stun 5", value=combined_value, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)
            
            elif stun5_field[1] == "`Empty`" and stun5_field[0] != user_mention and not any(field == user_mention for field in [stun0_field, shark_field, jelly_field, northtank_field, base_field]):
                stun5_field[1] = user_mention
                combined_value = "\n".join(stun5_field)

                embed.set_field_at(16, name="5️⃣ Stun 5", value=combined_value, inline=True)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)

            elif stun5_field[0] != f"`Empty`" and stun5_field[1] != f"`Empty`":
                await interaction.response.send_message(f"Someone else has signed up as 5️⃣ Stun 5!", ephemeral=True)
            elif any(field == user_mention for field in [jelly_field, base_field, stun0_field, northtank_field, shark_field]):
                await interaction.response.send_message(f"You are signed up as another incompatible role already!", ephemeral=True)
        except Exception as e:
            print(f"stun5button error(RaidsMenu): {e}") 
#endregion

#region dps button index 16
    @discord.ui.button(label=f"DPS", style=discord.ButtonStyle.blurple, emoji="⚔️", custom_id="raidsdps")
    async def dpsbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_id = interaction.user.id
            user_name = interaction.user.name
            user_mention = f"<@{interaction.user.id}> ({user_name})"

            message = interaction.message
            embed = message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            busc_field = embed_dict['fields'][3]['value']
            pt13_field = embed_dict['fields'][4]['value']
            pt2_field = embed_dict['fields'][5]['value']
            northcharge_field = embed_dict['fields'][6]['value']
            mainstun_field = embed_dict['fields'][7]['value']
            bustun_field = embed_dict['fields'][8]['value']
            northtank_field = embed_dict['fields'][9]['value']
            psntank_field = embed_dict['fields'][10]['value']
            cpr_field = embed_dict['fields'][11]['value']
            double_field = embed_dict['fields'][12]['value']
            jelly_field = embed_dict['fields'][13]['value']
            shark_field = embed_dict['fields'][14]['value']
            stun0_field = embed_dict['fields'][15]['value']
            stun5_field = embed_dict['fields'][16]['value'].split("\n")
            dps_field = embed_dict['fields'][17]['value'].split(", ")


            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)

            #region remove dps
            if user_mention in dps_field:
                self.remove_user(dps_field, user_mention, user_id)
                combined_value = ", ".join(dps_field)
                embed.set_field_at(17, name="⚔️ DPS", value=combined_value, inline=False)
                teamsize = functions.get_teamsize(embed)
                embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
                await interaction.response.edit_message(embed=embed)
                return
            #endregion

            if all(field != "`Empty`" for field in dps_field):
                await interaction.response.send_message("There is no more room for ⚔️ DPS", ephemeral=True)
                return
            
            if any(user_mention in field for field in stun5_field[:2]) or any(user_mention in field for field in [base_field, northtank_field, psntank_field, cpr_field, double_field, jelly_field, shark_field, stun0_field, busc_field, pt13_field, pt2_field, northcharge_field, mainstun_field, bustun_field]):
                await interaction.response.send_message("You don't need to sign up as ⚔️ DPS if you've signed up as a role already!", ephemeral=True)
                return
            
            self.add_user(dps_field, user_mention, user_id)
            combined_value = ", ".join(dps_field)
            embed.set_field_at(17, name="⚔️ DPS", value=combined_value, inline=False)
            teamsize = functions.get_teamsize(embed)
            embed.set_footer(text=f"Message ID: {message.id}  •  Team size {len(teamsize)}/10")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"dpsbutton error(RaidsMenu): {e}") 

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

