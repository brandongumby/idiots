#region  imports
# Standard library
import io

# Third-party libraries
import discord
from discord import app_commands
import requests
from easy_pil import *
from easy_pil import Editor, Font
from PIL import Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import asyncio

# custom modules
from util import myviews, config, functions, achievements, codebox, embeds, modals
#endregion


def load_commands(tree, client, TaskClass):
#system commands-------------------------------
#region  HELP
    @tree.command(name="help", description="shows how to view idiots bot commands")
    async def help(interaction: discord.Interaction):

        await interaction.response.send_message("type `/` then select idiots bot from the left side\n⬅️ or below (mobile) ⬇️ to view the commands", ephemeral=True)
#endregion
#region  add_react  add reaction role
    @tree.command(name="add_react", description="Add a reaction role (use in same channel as message)")
    @app_commands.describe(message_id = "enter the message id")
    @app_commands.describe(role = "enter the reaction role")
    @app_commands.describe(emoji = "enter the reaction emoji")
    @discord.app_commands.checks.has_permissions(manage_messages=True)
    async def add_react(interaction: discord.Interaction, message_id: str, role: str, emoji: str):
        try:
            await interaction.response.defer(ephemeral=True)
            message_id = int(message_id)
            role = int(role)
            async with client.db.cursor() as cursor:
                await cursor.execute("INSERT INTO react (message_id, role, emoji) VALUES (?, ?, ?)", (message_id, role, emoji,))
                await client.db.commit()

                channel = interaction.channel
                message = await channel.fetch_message(message_id)
                await message.add_reaction(emoji)

                await interaction.followup.send(f"Reaction role added!", ephemeral=True)
        except Exception as e:
            print(e)
    add_react.default_permissions = discord.Permissions(manage_messages=True)
#endregion
#region  clear command
    @tree.command(name="clear", description="purge an amount of messages")
    @app_commands.describe(amount_to_clear = "How many messages do you want to clear?")
    @discord.app_commands.checks.has_permissions(manage_messages=True)
    async def clear(interaction: discord.Interaction, amount_to_clear: int):
        await interaction.response.defer()
        await interaction.channel.purge(limit=amount_to_clear + 1)

    clear.default_permissions = discord.Permissions(manage_messages=True)
#endregion
#region  ticket creates ticket embed
    @tree.command(name="ticket", description="Creates a ticket embed.")
    @discord.app_commands.checks.has_permissions(manage_messages=True)
    async def ticket(interaction: discord.Interaction):
        tembed = discord.Embed(title="Create a Ticket!")
        tembed.add_field(name="Welcome to support tickets", value="To create a ticket click the button below\nAfter that it will create a ticket channel for you to be able to contact the Admin team directly.", inline=False)
        tembed.add_field(name="Ticket Use:", value=f"* Report any issues\n* Give us any feedback\n* Report discord users\n* Ask questions\n* Any other support you may need with the discord or clan")
        await interaction.response.send_message(embed=tembed, view=myviews.CreateTicket(client))

    ticket.default_permissions = discord.Permissions(manage_messages=True)
#endregion
#region  giveaway
    @tree.command(name="giveaway", description="creates a giveaway")
    async def giveaway(interaction: discord.Interaction):
        await interaction.response.send_modal(modals.GiveawayModal(client, TaskClass))
#endregion
#region  wiki
    @tree.command(name="wiki", description="link to rs wiki")
    @app_commands.describe(search = "What to look up")
    async def wiki(interaction: discord.Interaction, search: str):
        query = search.replace(' ', '%20')
    
        # Create the search URL
        url = f"https://runescape.wiki/w/Special:Search?search={query}&go=Go"
        
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        if response.status_code == 200:
            # If the request is successful, send the search URL to the Discord channel
            await interaction.response.send_message(f"Click here to search for **{search}**: [**Search Results**](<{url}>)")
        else:
            # If the request fails, send an error message
            await interaction.response.send_message("Something went wrong while searching. Please try again later.")
#endregion
#region  dropchance
    @tree.command(name="dropchance", description="simulates pet and item drops")
    async def dropchance(interaction: discord.Interaction):
        try:
            await interaction.response.send_modal(modals.DropChance())
        except Exception as e:
            print(e)

#endregion
#region  exec
    @tree.command(name="exec", description="Execute Python code")
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def exec(interaction: discord.Interaction):
        if interaction.user.id != config.OWNER:
            await interaction.response.send_message("⛔ You cannot use this.", ephemeral=True)
            return

        await interaction.response.send_modal(codebox.CodeModal())
    exec.default_permissions = discord.Permissions(administrator=True)
#endregion

#pof commands----------------------------------
#region  update_pof lender
    @tree.command(name="update_pof", description="Updates POF Lender")
    @app_commands.describe(animal = "enter animal type")
    @app_commands.choices(animal=[
        app_commands.Choice(name="Rabbit", value="rabbit"),
        app_commands.Choice(name="Chicken", value="chicken"),
        app_commands.Choice(name="Sheep", value="sheep"),
        app_commands.Choice(name="Cow", value="cow"),
        app_commands.Choice(name="Chinchompa", value="chinchompa"),
        app_commands.Choice(name="Spider", value="spider"),
        app_commands.Choice(name="Yak", value="yak"),
        app_commands.Choice(name="Zygomite", value="zygomite"),
        app_commands.Choice(name="Dragon", value="dragon"),
        app_commands.Choice(name="Frog", value="frog"),
        app_commands.Choice(name="Jadinko", value="jadinko"),
        app_commands.Choice(name="Salamander", value="salamander"),
        app_commands.Choice(name="Varanusaur", value="varanusaur"),
        app_commands.Choice(name="Arcane Apoterrasaur", value="arcane apoterrasaur"),
        app_commands.Choice(name="Brutish Dinosaur", value="brutish dinosaur"),
        app_commands.Choice(name="Scimitops", value="scimitops"),
        app_commands.Choice(name="Bagrada Rex", value="bagrada rex"),
        app_commands.Choice(name="Spicati Apoterrasaur", value="spicati apoterrasaur"),
        app_commands.Choice(name="Asciatops", value="asciatops"),
        app_commands.Choice(name="Corbicula Rex", value="corbicula rex"),
        app_commands.Choice(name="Oculi Apoterrasaur", value="oculi apoterrasaur"),
        app_commands.Choice(name="Malletops", value="malletops"),
        app_commands.Choice(name="Pavosaurus Rex", value="pavosaurus rex"),
    ])
    @app_commands.describe(owner = "enter the original owner's name")
    @app_commands.describe(lender = "enter the lender's name")
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def update_pof(interaction: discord.Interaction, animal: str, owner: str, lender: str):
        await interaction.response.defer(ephemeral=True)
        async with client.db.cursor() as cursor:
            await cursor.execute("UPDATE animals SET lender = ? WHERE animal = ? AND owner = ? AND guild = ?", (lender, animal, owner, interaction.guild.id,))
            await client.db.commit()
            await interaction.followup.send(f"{owner}'s {animal} has been updated to have {lender} as the Lender.", ephemeral=True)
        
    update_pof.default_permissions = discord.Permissions(administrator=True)
#endregion
#region  creates poflend embed
    @tree.command(name="pof_lend", description="Creates a pof lender embed.")
    @discord.app_commands.checks.has_permissions(manage_messages=True)
    async def pof_lend(interaction: discord.Interaction):
        pofembed = discord.Embed(title="Abbie's POF Lending")
        pofembed.set_thumbnail(url="https://runescape.wiki/images/Granny_Potterington.png?ec859")
        pofembed.add_field(name="Welcome to Abbie's POF Lending system", value="To view the status of our animals click the '**Check Animal Status**' button\nAfter that it will send you a dropdown to select which animals to check the status of.", inline=False)
        pofembed.add_field(name="How to Request a Lend", value=f"You can use the '**Request lend / support**' button to request a lend or if you need any other additional support.\nThis will create a POF Ticket for you to request a lend or ask questions.\nWe can hash out all the details in the ticket, like what animals you want to lend and when to meet up.")
        await interaction.response.send_message(embed=pofembed, view=myviews.CreatePOFTicket(client))

    pof_lend.default_permissions = discord.Permissions(manage_messages=True)
#endregion
#region  add_animal to poflend system
    @tree.command(name="add_animal", description="add new animal pair to the pof lending system")
    @app_commands.describe(animal = "enter animal type")
    @app_commands.choices(animal=[
        app_commands.Choice(name="Rabbit", value="rabbit"),
        app_commands.Choice(name="Chicken", value="chicken"),
        app_commands.Choice(name="Sheep", value="sheep"),
        app_commands.Choice(name="Cow", value="cow"),
        app_commands.Choice(name="Chinchompa", value="chinchompa"),
        app_commands.Choice(name="Spider", value="spider"),
        app_commands.Choice(name="Yak", value="yak"),
        app_commands.Choice(name="Zygomite", value="zygomite"),
        app_commands.Choice(name="Dragon", value="dragon"),
        app_commands.Choice(name="Frog", value="frog"),
        app_commands.Choice(name="Jadinko", value="jadinko"),
        app_commands.Choice(name="Salamander", value="salamander"),
        app_commands.Choice(name="Varanusaur", value="varanusaur"),
        app_commands.Choice(name="Arcane Apoterrasaur", value="arcane apoterrasaur"),
        app_commands.Choice(name="Brutish Dinosaur", value="brutish dinosaur"),
        app_commands.Choice(name="Scimitops", value="scimitops"),
        app_commands.Choice(name="Bagrada Rex", value="bagrada rex"),
        app_commands.Choice(name="Spicati Apoterrasaur", value="spicati apoterrasaur"),
        app_commands.Choice(name="Asciatops", value="asciatops"),
        app_commands.Choice(name="Corbicula Rex", value="corbicula rex"),
        app_commands.Choice(name="Oculi Apoterrasaur", value="oculi apoterrasaur"),
        app_commands.Choice(name="Malletops", value="malletops"),
        app_commands.Choice(name="Pavosaurus Rex", value="pavosaurus rex"),
    ])
    @app_commands.describe(breed1 = "enter the breed of first animal")
    @app_commands.describe(trait_a1 = "enter first trait of first animal")
    @app_commands.describe(trait_a2 = "enter second trait of first animal")
    @app_commands.describe(trait_a3 = "enter third trait of first animal")
    @app_commands.describe(breed2 = "enter the breed of second animal")
    @app_commands.describe(trait_b1 = "enter first trait of second animal")
    @app_commands.describe(trait_b2 = "enter second trait of second animal")
    @app_commands.describe(trait_b3 = "enter third trait of second animal")
    @app_commands.describe(owner = "enter the original owners name")
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def add_animal(interaction: discord.Interaction, animal: str, breed1: str, trait_a1: str, trait_a2: str, trait_a3: str, breed2: str, trait_b1: str, trait_b2: str, trait_b3: str, owner: str):
        await interaction.response.defer(ephemeral=True)
        
        async with client.db.cursor() as cursor:
            await cursor.execute("INSERT INTO animals (animal, guild, breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (animal, interaction.guild.id, breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, "available"))
            await client.db.commit()

            addpofembed = discord.Embed(title=f"Animal pair added!", description=f"Animal pair: **{animal}**")
            addpofembed.add_field(name=f"First {animal}", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
            addpofembed.add_field(name=f"Second {animal}", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
            addpofembed.add_field(name="", value=f"Oringal owner: **{owner}** | Lender: **available**", inline=False)
            await interaction.followup.send(embed=addpofembed, ephemeral=True)

    add_animal.default_permissions = discord.Permissions(administrator=True)
#endregion

#teamforming commands--------------------------
#region  teamforming embed command
    @tree.command(name="team", description="Creates a teamforming dropdown post.")
    @discord.app_commands.checks.has_permissions(manage_messages=True)
    async def team(interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.channel.purge(limit=1)
        embed = discord.Embed.from_dict(embeds.team_dict1)
        await interaction.channel.send("Click the dropdown to select a boss to host!", embed=embed, view=myviews.TeamformView(client))

    team.default_permissions = discord.Permissions(manage_messages=True)
#endregion
#region  add_user for teamforming
    @tree.command(name="add_user", description="adds user to teamforming post")
    @app_commands.describe(message_id = "Enter the message id")
    @app_commands.describe(role = "Which role to update")
    @app_commands.describe(user_to_add = "Enter user to add")
    async def add_user(interaction: discord.Interaction, message_id: str, role: str, user_to_add: str):
        channel_id = config.TEAMFORM_CHANNEL
        messageid = message_id  
        channel = client.get_channel(channel_id) 
        message = await channel.fetch_message(messageid)

        if message.embeds:
            embed = message.embeds[0] 
        else:
            return
        if embed.author.name == f"Hosted by {interaction.user.name}" or interaction.user.guild_permissions.manage_messages:
            field_name_to_find = role.lower()
            field_updated = False
            for index, field in enumerate(embed.fields):
                if field_name_to_find in field.name.lower():
                    if field.value == "`Empty`":
                        new_value = user_to_add
                    else:
                        if '\n' in field.value:  
                            value_as_list = field.value.split('\n')
                        elif ', ' in field.value:  
                            value_as_list = field.value.split(', ')
                        else:
                            value_as_list = [field.value]  

                        value_to_replace = "`Empty`" 
                        for i, val in enumerate(value_as_list):
                            if val == value_to_replace:
                                value_as_list[i] = user_to_add
                                field_updated = True
                                break 
                        else:
                            await interaction.response.send_message(f"{field.name} appears to already be full.", ephemeral=True)
                            return
                        if field.name == "⚔️ DPS":
                            new_value = ', '.join(value_as_list)
                        else:
                            new_value = '\n'.join(value_as_list)  

                    embed.set_field_at(index, name=field.name, value=new_value, inline=field.inline)
                    field_updated = True
                    break 
            if field_updated:
                await message.edit(embed=embed)
                await interaction.response.send_message(f"{field.name} updated successfully.", ephemeral=True)

            else:
                await interaction.response.send_message(f'There is no role found matching "{role}", please double check the form!', ephemeral=True)
        else:
            await interaction.response.send_message(f"You don't have permissions to add/remove with this form!", ephemeral=True)
#endregion
#region  remove_user for teamforming
    @tree.command(name="remove_user", description="removes user from teamforming post")
    @app_commands.describe(message_id = "Enter the message id")
    @app_commands.describe(role = "Which role to update")
    @app_commands.describe(user_to_remove = "Enter user to remove")
    async def remove_user(interaction: discord.Interaction, message_id: str, role: str, user_to_remove: str):
        channel_id = config.TEAMFORM_CHANNEL
        messageid = message_id  
        channel = client.get_channel(channel_id) 

        message = await channel.fetch_message(messageid)

        if message.embeds:
            embed = message.embeds[0]   
        else:
            return
    
        if embed.author.name == f"Hosted by {interaction.user.name}" or interaction.user.guild_permissions.manage_messages:
            field_name_to_find = role.lower()
            removed_user = user_to_remove.lower()
            field_updated = False
            for index, field in enumerate(embed.fields):
                if field_name_to_find in field.name.lower():
                    if removed_user == field.value.lower():
                        new_value = "`Empty`"
                    elif removed_user in field.value.lower() and field.value.lower().startswith("<@") and ", " not in field.value.lower():
                        new_value = "`Empty`"
                    else:
                        if '\n' in field.value and removed_user in field.value.lower():  
                            value_as_list = field.value.split('\n')
                        elif ', ' in field.value and removed_user in field.value.lower():  
                            value_as_list = field.value.split(', ')

                        value_to_replace = removed_user  
                        for i, val in enumerate(value_as_list):
                            if val == value_to_replace:
                                value_as_list[i] = "`Empty`"
                                field_updated = True
                                break  
                        else:
                            await interaction.response.send_message(f"I don't see {user_to_remove} under that role.", ephemeral=True)
                            print(field.value)
                            return
                        if field.name == "⚔️ DPS":
                            new_value = ', '.join(value_as_list)
                        else:
                            new_value = '\n'.join(value_as_list)  

                    embed.set_field_at(index, name=field.name, value=new_value, inline=field.inline)
                    field_updated = True
                    break
            if field_updated:
                await message.edit(embed=embed)
                await interaction.response.send_message(f"{field.name} updated successfully.", ephemeral=True)
            else:
                await interaction.response.send_message(f'There is no role found matching "{role}", please double check the form!', ephemeral=True)
        else:
            await interaction.response.send_message(f"You don't have permissions to add/remove with this form!", ephemeral=True)
#endregion

#qotd commands---------------------------------
#region  qotd leaderboards
    @tree.command(name="leaderboard", description="Shows you the QOTD Leaderboards")
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def leaderboard(interaction: discord.Interaction):
        await interaction.response.defer()
        try:
            async with client.db.cursor() as cursor:
                    await cursor.execute("SELECT qotd_points, user_id FROM users WHERE guild = ? ORDER BY qotd_points DESC LIMIT 15", (interaction.guild.id,))
                    data = await cursor.fetchall()
                    if data:
                        count = 1
                        leaderboard_list = []
                        for table in data:
                            if table[0] < 1:
                                continue
                            user = interaction.guild.get_member(table[1])
                            points = table[0]

                            leaderboard_list.append({
                                "rank": count,
                                "name": user.display_name,
                                "points": points
                            })
                            count += 1

                        image = Image.open("leaderboard.png")
                        editor = Editor(image)

                        #region first place
                        if len(leaderboard_list) > 0:
                            name = leaderboard_list[0]['name']
                            font = Font.poppins(size=60, variant="bold")
                            if len(name) > 12:
                                name = name[:12]
                                editor.text((350, 500), f"{name}...", font=font, color="white")
                                editor.text((725, 400), f"({leaderboard_list[0]['points']})", font=font, color="white")
                            else:
                                axisX = (591 - (len(name) * 20))
                                editor.text((axisX, 500), f"{name} ({leaderboard_list[0]['points']})", font=font, color="white")
                        #endregion

                        #region second place
                        if len(leaderboard_list) > 1:
                            font = Font.poppins(size=40, variant="bold")
                            name = leaderboard_list[1]['name']
                            if len(name) > 12:
                                name = name[:12]
                                editor.text((1110, 400), f"{name}...({leaderboard_list[1]['points']})", font=font, color="white")
                            else:
                                font = Font.poppins(size=45, variant="bold")
                                axisX = (1305 - (len(name) * 15))
                                editor.text((axisX, 400), f"{name} ({leaderboard_list[1]['points']})", font=font, color="white")
                        #endregion

                        #region third place
                        if len(leaderboard_list) > 2:
                            font = Font.poppins(size=40, variant="bold")
                            name = leaderboard_list[2]['name']
                            if len(name) > 12:
                                name = name[:12]
                                editor.text((1110, 540), f"{name}...({leaderboard_list[2]['points']})", font=font, color="white")
                            else:
                                font = Font.poppins(size=45, variant="bold")
                                axisX = (1305 - (len(name) * 15))
                                editor.text((axisX, 540), f"{name} ({leaderboard_list[2]['points']})", font=font, color="white")
                        #endregion

                        #region remaining places
                        if len(leaderboard_list) > 3:
                            count = leaderboard_list[3]['rank']
                            name = leaderboard_list[3]['name']
                            font = Font.poppins(size=35, variant="bold")
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((300, 660), f"{count}. {name} ({leaderboard_list[3]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 4:
                            count = leaderboard_list[4]['rank']
                            name = leaderboard_list[4]['name']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((300, 705), f"{count}. {name} ({leaderboard_list[4]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 5:
                            name = leaderboard_list[5]['name']
                            count = leaderboard_list[5]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((300, 750), f"{count}. {name} ({leaderboard_list[5]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 6:
                            name = leaderboard_list[6]['name']
                            count = leaderboard_list[6]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((300, 795), f"{count}. {name} ({leaderboard_list[6]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 7:
                            name = leaderboard_list[7]['name']
                            count = leaderboard_list[7]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((300, 840), f"{count}. {name} ({leaderboard_list[7]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 8:
                            name = leaderboard_list[8]['name']
                            count = leaderboard_list[8]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((300, 885), f"{count}. {name} ({leaderboard_list[8]['points']})", font=font, color="black")

                            #start right side
                        if len(leaderboard_list) > 9:
                            name = leaderboard_list[9]['name']
                            count = leaderboard_list[9]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((1000, 660), f"{count}. {name} ({leaderboard_list[9]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 10:
                            name = leaderboard_list[10]['name']
                            count = leaderboard_list[10]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((1000, 705), f"{count}. {name} ({leaderboard_list[10]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 11:
                            name = leaderboard_list[11]['name']
                            count = leaderboard_list[11]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((1000, 750), f"{count}. {name} ({leaderboard_list[11]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 12:
                            name = leaderboard_list[12]['name']
                            count = leaderboard_list[12]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((1000, 795), f"{count}. {name} ({leaderboard_list[12]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 13:
                            name = leaderboard_list[13]['name']
                            count = leaderboard_list[13]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((1000, 840), f"{count}. {name} ({leaderboard_list[13]['points']})", font=font, color="black")
                        if len(leaderboard_list) > 14:
                            name = leaderboard_list[14]['name']
                            count = leaderboard_list[14]['rank']
                            if len(name) > 20:
                                name = f"{name[:20]}..."
                            editor.text((1000, 885), f"{count}. {name} ({leaderboard_list[14]['points']})", font=font, color="black")
                        #endregion

                        buffer = io.BytesIO()
                        editor.image.save(buffer, format="PNG")
                        buffer.seek(0)

                        file = discord.File(fp=buffer, filename="modified_image.png")

                        await interaction.followup.send(file=file)
        except Exception as e:
            print(e)
    leaderboard.default_permissions = discord.Permissions(administrator=True)
#endregion

#context menu commands (right clicks)----------
#region  Give Achievement
#    @tree.context_menu(name="Give Achievement")
#    @discord.app_commands.checks.has_permissions(manage_messages=True)
#    async def give_ach(interaction: discord.Interaction, member: discord.Member):
#        try:
#            lists_dict = []
#            await functions.create_acc(client, member.id, member.display_name, interaction.guild_id)
#            target_user = await functions.load_user(client, member.id, interaction.guild_id)
#            uncompleted_list = achievements.fetch_uncomplete(target_user.achievements.completed)
#            if uncompleted_list == []:
#                await interaction.response.send_message("This user has completed all achievements!", ephemeral=True)
#                return
#            if len(uncompleted_list) > 25:
#                chunks = functions.chunk_list(uncompleted_list, 25)
#                lists_dict.append({"name": "Achievements 1", "list": chunks[0]})
#                if len(chunks) > 1:
#                    lists_dict.append({"name": "Achievements 2", "list": chunks[1]})
#                if len(chunks) > 2:
#                    lists_dict.append({"name": "Achievements 3", "list": chunks[2]})
#
#                await interaction.response.send_message("Select a list of Achievements to give out", ephemeral=True, view=myviews.AchievementViewMulti(client, lists_dict, target_user))
#            else:
#                await interaction.response.send_message("Select an Achievement to give", ephemeral=True, view=myviews.AchievementView(client, uncompleted_list, target_user))
#        except Exception as e:
#            print(f"Give Achievement (Context) error: {e}")
#    give_ach.default_permissions = discord.Permissions(manage_messages=True)
#endregion
#region  award drop points
#    @tree.context_menu(name="Award Drop Points")
#    @discord.app_commands.checks.has_permissions(manage_messages=True)
#    async def give_drop(interaction: discord.Interaction, message: discord.Message):
#        try:
#            target_user = await functions.load_user(client, message.author.id, message.guild.id)
#            view = myviews.DropAward(target_user, message)
#            if message.id in target_user.achievements.drops.logged:
#                await interaction.response.send_message("This drop has already been awarded!", ephemeral=True)
#                return
#            await interaction.response.send_message("What tier drop?", ephemeral=True, view=view)
#        except Exception as e:
#            print(f"award drop points (Context) error: {e}")
#    give_drop.default_permissions = discord.Permissions(manage_messages=True)
#endregion
#region  View Profile
#    @tree.context_menu(name="View Profile")
#    async def view_prof(interaction: discord.Interaction, member: discord.Member):
#        await interaction.response.defer(ephemeral=True)
#        user = await functions.load_user(client, member.id, interaction.guild_id)
#        if user.roles == []:
#            roles = "None logged"
#        else:
#            roles = ""
#            for role in list(user.roles):
#                roles += f"<@&{role}> | "
#            roles = roles.rstrip(" | ")
#        file = await functions.fetch_usercard(client, member, interaction.guild_id)
#        await interaction.followup.send(file=file, ephemeral=True)
#endregion
#region  Confirm Drop
    @tree.context_menu(name="Confirm Drop")
    @discord.app_commands.checks.has_permissions(manage_messages=True)
    async def confirm_drop(interaction: discord.Interaction, message: discord.Message):
        await interaction.response.defer(ephemeral=True)
        view=myviews.GodsEventDrops(client, message)

        await interaction.followup.send("Select the drop tier", ephemeral=True, view=view)
   
    confirm_drop.default_permissions = discord.Permissions(manage_messages=True)
#endregion


#region test
    @tree.command(name="test", description="tests")
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def test(interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            
            # Google Sheets setup
            scope = [
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive"
            ]
            creds = ServiceAccountCredentials.from_json_keyfile_name("util/service_account.json", scope)
            client = gspread.authorize(creds)
            sheet = client.open("testing").sheet1
            
            await asyncio.to_thread(sheet.update_acell, "C7", "New Value")
            await interaction.followup.send("sheet updated")
        except Exception as e:
            print(f"test error: {e}")

#endregion

