import discord
from util import buttons, functions


class HMAmasMenu(discord.ui.View):
    labels_to_disable = ["Base", "West Scarabs", "West Chains", "East Scarabs", "East Chains", "Green Lines", "Platformer (sub 2k)", "Heiroglyphs"]
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


#region  base button
    @discord.ui.button(label=f"Base", style=discord.ButtonStyle.blurple, emoji="🛡️", custom_id="amasbase")
    async def basebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            NW_field = embed_dict['fields'][3]['value']
            SW_field = embed_dict['fields'][4]['value']
            NE_field = embed_dict['fields'][5]['value']
            SE_field = embed_dict['fields'][6]['value']
            green_field = embed_dict['fields'][7]['value'].split(", ")
            field_list = [NW_field, SW_field, NE_field, SE_field]

            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            
            if user_mention in base_field:
                new_field = "`Empty`"
            elif base_field == "`Empty`" and not any(user == user_mention for user in field_list):
                new_field = user_mention
            elif base_field != f"`Empty`" and base_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🛡️ Base!", ephemeral=True)
                return
            elif base_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as an incompatible role!", ephemeral=True)
                return
            embed.set_field_at(2, name=f"🛡️ Base", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"basebutton error(HMAmasMenu): {e}")
#endregion

#region  West scarabs button
    @discord.ui.button(label=f"West Scarabs", style=discord.ButtonStyle.blurple, emoji="↖️", custom_id="westscarabs")
    async def westscarabs(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            NW_field = embed_dict['fields'][3]['value']
            SW_field = embed_dict['fields'][4]['value']
            NE_field = embed_dict['fields'][5]['value']
            SE_field = embed_dict['fields'][6]['value']
            green_field = embed_dict['fields'][7]['value'].split(", ")
            field_list = [base_field, SW_field, NE_field, SE_field]

            if len(functions.get_teamsize(embed)) == 5 and user_mention not in functions.get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in NW_field:
                new_field = "`Empty`"
            elif NW_field == "`Empty`" and not any(user == user_mention for user in field_list):
                new_field = user_mention
            elif NW_field != f"`Empty`" and NW_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ↖️ West Scarabs!", ephemeral=True)
                return
            elif NW_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as an incompatible role!", ephemeral=True)
                return

            embed.set_field_at(3, name="↖️ West Scarabs", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"westscarabs error(HMAmasMenu): {e}")
#endregion

#region  West chains button
    @discord.ui.button(label=f"West Chains", style=discord.ButtonStyle.blurple, emoji="↙️", custom_id="westchains")
    async def westchains(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            NW_field = embed_dict['fields'][3]['value']
            SW_field = embed_dict['fields'][4]['value']
            NE_field = embed_dict['fields'][5]['value']
            SE_field = embed_dict['fields'][6]['value']
            green_field = embed_dict['fields'][7]['value'].split(", ")
            field_list = [base_field, NW_field, NE_field, SE_field]

            if len(functions.get_teamsize(embed)) == 5 and user_mention not in functions.get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in SW_field:
                new_field = "`Empty`"
            elif SW_field == "`Empty`" and not any(user == user_mention for user in field_list):
                new_field = user_mention
            elif SW_field != f"`Empty`" and SW_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ↙️ West Chains!", ephemeral=True)
                return
            elif SW_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as an incompatible role!", ephemeral=True)
                return

            embed.set_field_at(4, name="↙️ West Chains", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"westchains error(HMAmasMenu): {e}")
#endregion

#region  east scarabs button
    @discord.ui.button(label=f"East Scarabs", style=discord.ButtonStyle.blurple, emoji="↗️", custom_id="eastscarabs")
    async def eastscarabs(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            NW_field = embed_dict['fields'][3]['value']
            SW_field = embed_dict['fields'][4]['value']
            NE_field = embed_dict['fields'][5]['value']
            SE_field = embed_dict['fields'][6]['value']
            green_field = embed_dict['fields'][7]['value'].split(", ")
            field_list = [base_field, NW_field, SW_field, SE_field]

            if len(functions.get_teamsize(embed)) == 5 and user_mention not in functions.get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in NE_field:
                new_field = "`Empty`"
            elif NE_field == "`Empty`" and not any(user == user_mention for user in field_list):
                new_field = user_mention
            elif NE_field != f"`Empty`" and NE_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ↗️ East Scarabs!", ephemeral=True)
                return
            elif NE_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as an incompatible role!", ephemeral=True)
                return

            embed.set_field_at(5, name="↗️ East Scarabs", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"eastscarabs error(HMAmasMenu): {e}")
#endregion

#region  east chains button
    @discord.ui.button(label=f"East Chains", style=discord.ButtonStyle.blurple, emoji="↘️", custom_id="eastchains")
    async def eastchains(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            base_field = embed_dict['fields'][2]['value']
            NW_field = embed_dict['fields'][3]['value']
            SW_field = embed_dict['fields'][4]['value']
            NE_field = embed_dict['fields'][5]['value']
            SE_field = embed_dict['fields'][6]['value']
            green_field = embed_dict['fields'][7]['value'].split(", ")
            field_list = [base_field, NW_field, SW_field, NE_field]

            if len(functions.get_teamsize(embed)) == 5 and user_mention not in functions.get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in SE_field:
                new_field = "`Empty`"
            elif SE_field == "`Empty`" and not any(user == user_mention for user in field_list):
                new_field = user_mention
            elif SE_field != f"`Empty`" and SE_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ↘️ East Chains!", ephemeral=True)
                return
            elif SE_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as an incompatible role!", ephemeral=True)
                return

            embed.set_field_at(6, name="↘️ East Chains", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"eastchains error(HMAmasMenu): {e}")
#endregion

#region  green lines button
    @discord.ui.button(label=f"Green Lines", style=discord.ButtonStyle.blurple, emoji="🟩", custom_id="greenlines")
    async def greenlines(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            green_field = embed_dict['fields'][7]['value'].split(", ")

            if len(functions.get_teamsize(embed)) == 5 and user_mention not in functions.get_teamsize(embed):
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return

            if user_mention in green_field:
                functions.team_removeuser(green_field, user_mention)
                combined_value = ", ".join(green_field)
                new_field = combined_value
            elif all(field != "`Empty`" for field in green_field):
                await interaction.response.send_message("There is no more room for 🟩 Green Lines", ephemeral=True)
                return
            else:
                functions.team_adduser(green_field, user_mention)
                combined_value = ", ".join(green_field)
                new_field = combined_value
            embed.set_field_at(7, name="🟩 Green Lines", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"greenlines error(HMAmasMenu): {e}")
#endregion

#region  platformer button
    @discord.ui.button(label=f"Platformer (sub 2k)", style=discord.ButtonStyle.blurple, emoji="⤴️", custom_id="platformer")
    async def platformer(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            platform_field = embed_dict['fields'][8]['value']
            heiroglyph_field = embed_dict['fields'][9]['value']
            field_list = [heiroglyph_field]

            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            
            if user_mention in platform_field:
                new_field = "`Empty`"
            elif platform_field == "`Empty`" and not any(user == user_mention for user in field_list):
                new_field = user_mention
            elif platform_field != f"`Empty`" and platform_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as ⤴️ Platformer (sub 2k)!", ephemeral=True)
                return
            elif platform_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as an incompatible role!", ephemeral=True)
                return
            embed.set_field_at(8, name=f"⤴️ Platformer (sub 2k)", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"platformer error(HMAmasMenu): {e}")
#endregion

#region  Heiroglyphs button
    @discord.ui.button(label=f"Heiroglyphs", style=discord.ButtonStyle.blurple, emoji="🔣", custom_id="Heiroglyphs")
    async def Heiroglyphs(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            teamsize = functions.get_teamsize(embed)
            embed_dict = embed.to_dict()
            platform_field = embed_dict['fields'][8]['value']
            heiroglyph_field = embed_dict['fields'][9]['value']
            field_list = [platform_field]

            if len(teamsize) == 5 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            
            if user_mention in heiroglyph_field:
                new_field = "`Empty`"
            elif heiroglyph_field == "`Empty`" and not any(user == user_mention for user in field_list):
                new_field = user_mention
            elif heiroglyph_field != f"`Empty`" and heiroglyph_field != user_mention:
                await interaction.response.send_message(f"Someone else has signed up as 🔣 Heiroglyphs!", ephemeral=True)
                return
            elif heiroglyph_field == "`Empty`" and any(field == user_mention for field in field_list):
                await interaction.response.send_message(f"You are signed up as an incompatible role!", ephemeral=True)
                return
            embed.set_field_at(9, name=f"🔣 Heiroglyphs", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(functions.get_teamsize(embed))}/5")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"Heiroglyphs error(HMAmasMenu): {e}")
#endregion
