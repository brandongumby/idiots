#region  imports
# Standard library
import io
import re
import json
import time
import random
import textwrap
import asyncio
import calendar
from datetime import datetime, timezone

# Third-party libraries
import discord
from discord import NotFound
import requests
from easy_pil import *
from easy_pil import Editor, Font
from PIL import Image

# custom modules
from util import myviews, config, objects
#endregion


#system functions---------------------------
#region  get_time
async def get_time(time_input):
    output_time = time.strptime(time_input, '%Y-%m-%d %H:%M:%S.%f%z')
    naive_datetime = datetime(*output_time[:6])
    new_time = calendar.timegm(naive_datetime.timetuple())
    return new_time
#endregion
#region  fetch_all_messages
async def fetch_all_messages(channel, limit=None):
    messages = []
    async for message in channel.history(limit=limit, oldest_first=True):
        messages.append(message)
    return messages
#endregion
#region  remove_parentheses
def remove_parentheses(text):
    cleaned_text = re.sub(r'\s*\(.*?\)', '', text)
    return cleaned_text
#endregion
#region  add_react_role
async def add_react_role(client, react_data):
    try:
        message_id = react_data.get('message_id')
        user_id = react_data.get('user_id')
        emoji = react_data.get('emoji')
        guild_id = react_data.get('guild_id')
        guild = client.get_guild(guild_id)
        member = guild.get_member(user_id)
        emoji = str(emoji)

        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT role FROM react WHERE message_id = ? AND emoji = ?", (message_id, emoji,))
            role_id = await cursor.fetchone()
            if role_id is None:
                return
            else:
                role_id = role_id[0]
                role = discord.utils.get(guild.roles, id=role_id)
                await member.add_roles(role)
    except Exception as e:
          print(f"add_react_role error: {e}")
#endregion
#region  remove_react_role
async def remove_react_role(client, react_data):
    try:
        message_id = react_data.get('message_id')
        user_id = react_data.get('user_id')
        emoji = react_data.get('emoji')
        guild_id = react_data.get('guild_id')
        guild = client.get_guild(guild_id)
        member = guild.get_member(user_id)
        emoji = str(emoji)

        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT role FROM react WHERE message_id = ? AND emoji = ?", (message_id, emoji,))
            role_id = await cursor.fetchone()
            if role_id is None:
                return
            else:
                role_id = role_id[0]
                role = discord.utils.get(guild.roles, id=role_id)
                await member.remove_roles(role)
    except Exception as e:
          print(f"remove_react_role error: {e}")
#endregion
#region  cache_message
async def cache_message(client, message_data):
    try:
#message_data = {"message_id": message.id, "content": message.content,"guild": message.guild.id, "user_id": message.author.id, "username": message.author.name, "created_at": message_time_unix}
        message_id = message_data.get('message_id')
        guild = message_data.get('guild')
        content = message_data.get('content')
        user_id = message_data.get('user_id')
        username = message_data.get('username')
        created_at = message_data.get('created_at')
        async with client.db.cursor() as cursor:
            await cursor.execute("INSERT INTO messages (user, username, message_id, guild, content, created_at) VALUES (?, ?, ?, ?, ?, ?)", (user_id, username, message_id, guild, content, created_at,))
            await client.db.commit()
    except Exception as e:
          print(f"cache_message error: {e}")
#endregion
#region  edit_cache_message
async def edit_cache_message(client, message_data):
    try:
        logs_channel = client.get_channel(config.LOGS_CHANNEL)
        message_id_set = message_data.get('message_id')
        message_id = next(iter(message_id_set))
        content_set = message_data.get('content')
        content = next(iter(content_set))
        user_id_set = message_data.get('user_id')
        user_id = next(iter(user_id_set))
        username_set = message_data.get('username')
        username = next(iter(username_set))

        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT content FROM messages WHERE message_id = ? AND user = ?", (message_id, user_id,))
            old_content = await cursor.fetchone()
            if old_content:
                old_content = old_content[0]
            else:
                 return

            await cursor.execute("UPDATE messages SET content = ? WHERE message_id = ? AND user = ?", (content, message_id, user_id,))
            await client.db.commit()

        edit_embed = discord.Embed( title="Message Edited", description=f"message edited by {username}", color=0x1a1aff)
        edit_embed.add_field(name="**Before:**", value=f"{old_content}", inline=False)
        edit_embed.add_field(name="**After:**", value=f"{content}", inline=False)

        await logs_channel.send(embed=edit_embed)
    except Exception as e:
          print(f"edit_cache_message error: {e}")
#endregion
#region  delete_message
#message_data = {"message_id": message_id, "user_id": author_id, "username": author_name,}
async def delete_message(client, message_data):
    try:
        logs_channel = client.get_channel(config.LOGS_CHANNEL)
        message_id = message_data.get('message_id')
        channel_id = message_data.get('channel_id')

        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT content, username FROM messages WHERE message_id = ?", (message_id,))
            row = await cursor.fetchone()
            if row:
                old_content, username = row
            else:
                return

            dltembed = discord.Embed(title="Message Deleted", description=f"Message deleted from {username} in <#{channel_id}>", color=0xff0000)
            dltembed.add_field(name="**Message content:**", value=old_content or "No content")
            await logs_channel.send(embed=dltembed)
    except Exception as e:
          print(f"delete_message error: {e}")
#endregion
#region  gain_xp
async def gain_xp(client, user_id, guild_id):
    try:
        user = await load_user(client, user_id, guild_id)

        if user.level < 5:
            user.xp += random.randint(1, 5)
        else:
            rand = random.randint(1, (user.level//10))
            if rand == 1:
                user.xp += random.randint(1, 5)
        if user.xp >= 100:
                user.level += 1
                user.xp = 0
        await user.save()
    except Exception as e:
          print(f"gain_xp error: {e}")
#endregion
#region  PurgeOldMessage
async def PurgeOldMessage(client):
    try:
        now_unix = int(datetime.now(timezone.utc).timestamp())
        time_ago = now_unix - (2592000 * 2) #last number is months 
        async with client.db.cursor() as cursor:
            await cursor.execute("DELETE FROM messages WHERE created_at < ?", (time_ago,))
            await client.db.commit()
    except Exception as e:
        print(f"PurgeOldMessage error: {e}")
#endregion
#region  fetch_giveaways
async def fetch_giveaways(client, TaskClass):
    try:
        channel = client.get_channel(config.GIVEAWAYS)
        now_unix = int(datetime.now(timezone.utc).timestamp())

        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT end_time, message_id FROM giveaways WHERE end_time = (SELECT MIN(end_time) FROM giveaways WHERE finished = ?)", ("False",))
            row = await cursor.fetchone()

            if row is None:
                return

            end_time, message_id = row
            message = await channel.fetch_message(message_id)

            if end_time < now_unix:
                delay = 0
            else:
                delay = (end_time - now_unix)
            await asyncio.sleep(delay)

            await cursor.execute("SELECT end_time, prize, participants, message_id, description, host, winners FROM giveaways WHERE end_time = (SELECT MIN(end_time) FROM giveaways WHERE finished = ?)", ("False",))
            end_time, prize, part_json, message_id, description, host, winners = await cursor.fetchone()

            if part_json:
                participants = json.loads(part_json)
            else:
                entries = "no participants found"
                winner = "No Winner"
            if winners == 1 and part_json:
                winner = f"<@{random.choice(participants)}>"
                entries = len(participants)
            else:
                winner_list = []
                for _ in range(winners):
                    if len(participants) == 0:
                        break
                    chosen_winner = random.choice(participants)
                    winner_list.append(f"<@{chosen_winner}>")
                    participants.remove(chosen_winner)
                    entries = (len(participants) + winners)
                
                winner = ", ".join(winner_list)
            
            embed = discord.Embed(title="🎉 Idiots Giveaway! 🎉", description=f"{description}", color=0x2986cc)
            embed.add_field(name=f"", value=f"Prize: **{prize}**", inline=False)
            embed.add_field(name="", value=f"Ended: <t:{end_time}:R> (<t:{end_time}:f>)\nHosted by: <@{host}>\nEntries: **{entries}**\nWinners: {winner}", inline=False)
            embed.set_thumbnail(url="https://i.imgur.com/tgQRu7a.png")
            view=myviews.GiveawayEnd(client, TaskClass)
            await message.edit(embed=embed, view=view)
            await channel.send(f"🎉Congratulations to {winner} on winning **{prize}**!")

            await cursor.execute("UPDATE giveaways SET finished = ? WHERE message_id = ?", ("True", message_id,))
            await client.db.commit()

        await StartTask(TaskClass)
    except Exception as e:
        print(f"fetch_giveaways error: {e}")
#endregion
#region  StartTask
async def StartTask(TaskClass):
    try:
        if TaskClass.give_not_done():
            TaskClass.give.cancel()
        TaskClass.start_task()
    except Exception as e:
        print(f"StartTask error: {e}")
#endregion
#region  set_activity
async def set_activity(client):
    try:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/help"))
    except Exception as e:
        print(f"set_activity error: {e}")
#endregion

#teamfrom functions--------------------------
#region  teamform_ping
async def teamform_ping(client, message, interaction, boss, new_time):
    try:
        message_url = message.jump_url 
        target_channel = interaction.guild.get_channel(config.DISCUSSION_CHANNEL)
        if boss == 1:
            role = "<@&889687198406959135>"
            rules = "**Seismic weapons & energies are SPLIT** *(unless stated otherwise and agreed upon)*"
        elif boss == 2:
            role = "<@&889687198385995802>"
            rules = "**Codex are SPLIT and weapons/chests are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 3:
            role = "<@&1160963385442181213> <@&889687198406959135>"
            rules = "**Seismic weapons are SPLIT & energies/commons are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 4:
            role = "<@&893509368807579658>"
            rules = "**All drops are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 5:
            role = "<@&893509272707678208>"
            rules = "**Staff pieces are SPLIT & all other drops are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 6:
            role = "<@&906730570535546960>"
            rules = "**ALL drops are KEEPS**"
        elif boss == 7:
            role = "<@&889687198406959136>"
            rules = "**ALL drops are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 8:
            role = "<@&889687198385995803>"
            rules = "**Bows and grims are SPLIT everything else is KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 9:
            role = "<@&1179332987129696277>"
            rules = "**ALL drops are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 10:
            role = "<@&993855405530824704>"
            rules = "**ALL drops are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 11:
            role = "<@&1260656212656263168>"
            rules = "**ALL drops are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 12:
            role = "<@&1286091200767721562>"
            rules = "**ALL drops are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 13:
            role = "<@&906732539765465150> <@&906732576755048448> <@&906732580861247539>"
            rules = "**ALL drops are KEEPS** *(unless stated otherwise and agreed upon)*"
        elif boss == 14:
            role = "<@&1396592677729992870>"
            rules = "**ALL drops are SPLITS *(for now)*** *(unless stated otherwise and agreed upon)*"

        await target_channel.send(f"{role} Sign up posted!  <t:{new_time}:F>\n [LINK]({message_url}) to the signup!\nHosted by: <@{interaction.user.id}>\n{rules}\nRules: <#1271568914538827807>")
    except Exception as e:
        print(f"teamform_ping error: {e}")
#endregion
#region  team_adduser
def team_adduser(field, user_mention):
    for i in range(len(field)):
        if field[i] == "`Empty`":
            field[i] = user_mention
            break
#endregion
#region  team_removeuser
def team_removeuser(field, user_mention):
    for i in range(len(field)):
        if field[i] == user_mention:
            field[i] = "`Empty`"
            break
#endregion
#region  store_user_roles
async def store_user_roles(client, user_id, guild_id):
    try:
        guild = client.get_guild(guild_id)
        member = guild.get_member(user_id)

        if not member:  # fallback if not cached
            member = await guild.fetch_member(user_id)

        roles = member.roles 
        user = await load_user(client, user_id, guild_id)
        role_ids = [role.id for role in roles if not role.is_default()]

        user.roles = role_ids
        await user.save()
    except Exception as e:
          print(f"store_user_roles error: {e}")
#endregion
#region  get_teamsize
def get_teamsize(embed):
    fields = []
    for index, field in enumerate(embed.fields):
        if index == 0:
            continue 
        if index == 1:
            continue 
        if index == len(embed.fields) - 1:
            continue 
        if '\n' in field.value:
            value_as_list = field.value.split('\n')
        elif ', ' in field.value:
            value_as_list = field.value.split(', ')
        else:
            value_as_list = [field.value]
        for val in value_as_list:
            cleaned_val = val.strip()
            if cleaned_val != "`Empty`":
                fields.append(cleaned_val)

    teamsize = set(fields)
    return teamsize
#endregion

#qotd functions------------------------------
#region  update_leaderboard
async def update_leaderboard(client):
    try:
        guild = client.get_guild(config.GUILD_ID)
        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT qotd_points, user_id FROM users WHERE guild = ? ORDER BY qotd_points DESC LIMIT 15", (config.GUILD_ID,))
            data = await cursor.fetchall()
            if data:
                count = 1
                leaderboard_list = []
                for table in data:
                    if table[0] < 1:
                        continue
                    user = guild.get_member(table[1])
                    points = table[0]

                    leaderboard_list.append({
                        "rank": count,
                        "name": user.display_name,
                        "points": points
                    })
                    count += 1

                image = Image.open("assets/leaderboard.png")
                editor = Editor(image)

                #region no points
                if len(leaderboard_list) < 1:
                    font = Font.poppins(size=80, variant="bold")
                    editor.text((275, 795), f"Leaderboards are currently empty.", font=font, color="black")
                #endregion

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
                channel = client.get_channel(config.QOTD_CHANNEL)
                message = await channel.fetch_message(config.QOTD_LEADERBOARD)

                await message.edit(attachments=[file])
    except Exception as e:
        print(f"update_leaderboard error: {e}")
#endregion
#region  qotd_gratz
async def qotd_gratz(client):
    try:
        guild = client.get_guild(config.GUILD_ID)
        role = discord.utils.get(guild.roles, id=config.QOTD_ROLE)

        if role is None:
            print("Role not found!")
        else:
            for member in role.members:
                await member.remove_roles(role, reason="role removal for qotd")
        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT user_id FROM users WHERE guild = ? ORDER BY qotd_points DESC LIMIT 3", (config.GUILD_ID,))
            rows = await cursor.fetchall()
            if not rows:
                return
            winners = [row[0] for row in rows[:3]]
            while len(winners) < 3:
                winners.append(None)
            first, second, third = winners

            winner = guild.get_member(first)
            if first:
                first_place = await load_user(client, first, config.GUILD_ID)
                first_place.qotd.wins += 1
                first_place.qotd.top_3 += 1
                await first_place.save()
            if second:
                second_place = await load_user(client, second, config.GUILD_ID)
                second_place.qotd.top_3 += 1
                await second_place.save()
            if third:
                third_place = await load_user(client, third, config.GUILD_ID)
                third_place.qotd.top_3 += 1
                await third_place.save()

            messages = [
                f"Hey <@{first}>! You did it! 🥇\nYou crushed the Question of the Day and snagged the <@&{config.QOTD_ROLE}> like a boss 😎\nEnjoy your reign as trivia royalty 👑✨",
                f"🎓 <@{first}> has risen above the rest!\nWith wisdom, wit, and unstoppable drive, you've earned the coveted <@&{config.QOTD_ROLE}> for last month’s QOTD!\nLet the accolades flow—your brilliance shines bright 💫🏆",
                f"🌟 Congratulations, <@{first}>! 🌟\nYou've claimed the crown and earned the <@&{config.QOTD_ROLE}> for dominating last month’s QOTD!\n 🧠💥🏅 Smart answers, fast reflexes, and relentless consistency—you're the ultimate quiz master! 👑🎉",
            ]

            await cursor.execute("SELECT user_id, data FROM users WHERE guild = ?", (config.GUILD_ID,))
            rows = await cursor.fetchall()

            for user_id, data in rows:
                user = await load_user(client, user_id, config.GUILD_ID)
                user.qotd.points = 0
                await user.save()
                await cursor.execute("UPDATE users SET qotd_points = ? WHERE user_id = ? AND guild = ?", (0, user_id, config.GUILD_ID))
            await client.db.commit()

            await update_leaderboard(client)

            channel = client.get_channel(config.QOTD_CHANNEL)
            new_msg = random.choice(messages)
            update_msg = await channel.send(new_msg)

            await cursor.execute("SELECT gratz_message_id FROM qotd WHERE guild = ?", (config.GUILD_ID,))
            row = await cursor.fetchone()

            if row is None:
                await cursor.execute("INSERT INTO qotd (gratz_message_id, guild) VALUES (?, ?)", (update_msg.id, config.GUILD_ID))
            else:
                try:
                    msg = await channel.fetch_message(row[0])
                    await msg.delete()
                except Exception:
                    pass
                await cursor.execute("UPDATE qotd SET gratz_message_id = ? WHERE guild = ?", (update_msg.id, config.GUILD_ID))

            await client.db.commit()
            await winner.add_roles(role, reason="Assigning role to user")
    except Exception as e:
        print(f"qotd_gratz error: {e}")
#endregion
#region  send_qotd
async def send_qotd(client):
    try:
        async with client.db.cursor() as cursor:
            is_old = True
            while is_old:
                response = requests.get("https://the-trivia-api.com/api/questions?limit=1")
                data = response.json()
                if data:
                    first_item = data[0]
                    question_text = first_item['question']
                    correct_answer = first_item['correctAnswer']
                    difficulty = first_item['difficulty']
                    wrong_answer = first_item['incorrectAnswers']

                    correct = correct_answer
                    incorrect = wrong_answer
                    tagged_answers = [(correct, 'correct')] + \
                                        [(item, 'wrong') for item in incorrect]
                    
                    await cursor.execute("SELECT 1 FROM questions WHERE question = ? AND guild = ?", (question_text, config.GUILD_ID))
                    exists = await cursor.fetchone()
                    
                    if not exists:
                        await cursor.execute("INSERT INTO questions (question, guild) VALUES (?, ?)", (question_text, config.GUILD_ID))
                        await client.db.commit()
                        is_old = False
                
            random.shuffle(tagged_answers)

            await cursor.execute("UPDATE qotd SET tagged = ?, correct = ?, difficulty = ? WHERE guild = ?", (json.dumps(tagged_answers), json.dumps(correct), json.dumps(difficulty), config.GUILD_ID))
            await client.db.commit()

            qotd_view = myviews.QotdView(client, tagged_answers, correct, difficulty)

            try:
                image = Image.open("assets/qotd.png")
            except Exception as e:
                print(e)
            editor = Editor(image)
            question = question_text
            answerA = tagged_answers[0][0]
            answerB = tagged_answers[1][0]
            answerC = tagged_answers[2][0]
            answerD = tagged_answers[3][0]

            font = Font.poppins(size=40, variant="bold")
            #region Add question
            if 142 > len(question) > 76:
                wrapped_lines = textwrap.wrap(question, width=76)
                editor.text((200, 350), wrapped_lines[0], font=font, color="white")
                editor.text((200, 400), wrapped_lines[1], font=font, color="white")
            elif len(question) > 142:
                wrapped_lines = textwrap.wrap(question, width=76)
                editor.text((200, 330), wrapped_lines[0], font=font, color="white")
                editor.text((200, 375), wrapped_lines[1], font=font, color="white")
                editor.text((200, 420), wrapped_lines[2], font=font, color="white")
            else:
                editor.text((200, 380), question, font=font, color="white")
            #endregion

            #region Add difficulty
            editor.text((850, 260), f"difficulty: {difficulty}", font=font, color="black")
            #endregion

            #region Add AnswerA
            if 60 > len(answerA) > 30:
                wrapped_ansA = textwrap.wrap(answerA, width=30)
                editor.text((325, 570), wrapped_ansA[0], font=font, color="black")
                editor.text((325, 620), wrapped_ansA[1], font=font, color="black")
            elif len(answerA) > 60:
                wrapped_ansA = textwrap.wrap(answerA, width=30)
                editor.text((325, 550), wrapped_ansA[0], font=font, color="black")
                editor.text((325, 595), wrapped_ansA[1], font=font, color="black")
                editor.text((325, 640), wrapped_ansA[2], font=font, color="black")
            else:
                editor.text((325, 595), answerA, font=font, color="black")
            #endregion

            #region Add AnswerB
            if 60 > len(answerB) > 30:
                wrapped_ansB = textwrap.wrap(answerB, width=30)
                editor.text((1150, 570), wrapped_ansB[0], font=font, color="black")
                editor.text((1150, 620), wrapped_ansB[1], font=font, color="black")
            elif len(answerB) > 60:
                wrapped_ansB = textwrap.wrap(answerB, width=30)
                editor.text((1150, 550), wrapped_ansB[0], font=font, color="black")
                editor.text((1150, 595), wrapped_ansB[1], font=font, color="black")
                editor.text((1150, 640), wrapped_ansB[2], font=font, color="black")
            else:
                editor.text((1150, 595), answerB, font=font, color="black")
            #endregion

            #region Add AnswerC
            if 60 > len(answerC) > 30:
                wrapped_ansC = textwrap.wrap(answerC, width=30)
                editor.text((325, 795), wrapped_ansC[0], font=font, color="black")
                editor.text((325, 845), wrapped_ansC[1], font=font, color="black")
            elif len(answerC) > 60:
                wrapped_ansC = textwrap.wrap(answerC, width=30)
                editor.text((325, 775), wrapped_ansC[0], font=font, color="black")
                editor.text((325, 820), wrapped_ansC[1], font=font, color="black")
                editor.text((325, 865), wrapped_ansC[2], font=font, color="black")
            else:
                editor.text((325, 820), answerC, font=font, color="black")
            #endregion

            #region Add AnswerD
            if 60 > len(answerD) > 30:
                wrapped_ansD = textwrap.wrap(answerD, width=30)
                editor.text((1150, 795), wrapped_ansD[0], font=font, color="black")
                editor.text((1150, 845), wrapped_ansD[1], font=font, color="black")
            elif len(answerD) > 60:
                wrapped_ansD = textwrap.wrap(answerD, width=30)
                editor.text((1150, 775), wrapped_ansD[0], font=font, color="black")
                editor.text((1150, 820), wrapped_ansD[1], font=font, color="black")
                editor.text((1150, 865), wrapped_ansD[2], font=font, color="black")
            else:
                editor.text((1150, 820), answerD, font=font, color="black")
            #endregion

            # Save to memory
            buffer = io.BytesIO()
            editor.image.save(buffer, format="PNG")
            buffer.seek(0)

            file = discord.File(fp=buffer, filename="modified_image.png")

            channel = client.get_channel(config.QOTD_CHANNEL)
            message = await channel.send(f"<@&1131915330344718376>", file=file, view=qotd_view)
            await delete_qotd(client, message.id)
    except Exception as e:
        print(f"send_qotd error: {e}")
#endregion
#region  delete_qotd
async def delete_qotd(client, message_id):
    try:
        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT message_id FROM qotd WHERE guild = ?", (config.GUILD_ID,))
            exists = await cursor.fetchone()
            
            if exists:
                await cursor.execute("UPDATE qotd SET message_id = ? WHERE guild = ?", (message_id, config.GUILD_ID))
                try:
                    channel = client.get_channel(config.QOTD_CHANNEL)
                    msg = await channel.fetch_message(int(exists[0]))
                    await msg.delete()
                except Exception as e:
                     print(f"delete_qotd error(await msg.delete()): {e}")
            else:
                await cursor.execute("INSERT INTO qotd (message_id, guild) VALUES (?, ?)", (message_id, config.GUILD_ID))
            
            await client.db.commit()
    except Exception as e:
        print(f"delete_qotd error: {e}")
#endregion

#user functions------------------------------
#region  create_acc
async def create_acc(client, user_id, display_name, guild_id):
    try:
        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT data FROM users WHERE user_id = ? AND guild =?", (user_id, guild_id))
            user = await cursor.fetchone()
            if user is None:
                new_user = objects.User(client, display_name, user_id, guild_id, roles=[])
                await new_user.save()
                await store_user_roles(client, user_id, guild_id)
                await cursor.execute("UPDATE users SET qotd_points = ? WHERE user_id = ? AND guild = ?", (0, user_id, guild_id))
                await client.db.commit()
            else:
                return
    except Exception as e:
        print(f"create_acc error: {e}")
#endregion
#region  load_user
async def load_user(client, user_id, guild_id):
    try:
        guild = client.get_guild(guild_id)
        member = await guild.fetch_member(user_id)
        await create_acc(client, user_id, member.display_name, guild_id)
        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT data FROM users WHERE user_id = ? AND guild = ?", (user_id, guild_id))
            row = await cursor.fetchone()
        if row:
            data = json.loads(row[0])
            return objects.User.from_dict(client, data)
        return None
    except Exception as e:
        print(f"load_user error: {e}")
#endregion
#region  send_usercard
async def fetch_usercard(client, member, guild_id):
    try:
        user = await load_user(client, member.id, guild_id)

        usercards = [
            "assets/usercards/usrcard1.png",
            "assets/usercards/usrcard2.png",
            "assets/usercards/usrcard3.png",
            "assets/usercards/usrcard4.png",
            "assets/usercards/usrcard5.png",
            "assets/usercards/usrcard6.png",
        ]
        selected = random.choice(usercards)
        image = Image.open(selected)

        editor = Editor(image)

        #region added text

        #add name
        name = user.name

        if len(name) > 16:
            name = name[:16]
        font = Font.poppins(size=30, variant="bold")
        editor.text((110, 23), name, font=font, color="white")

        #add id
        id = str(user.id)
        font = Font.poppins(size=20)
        editor.text((535, 38), id, font=font, color="white")

        #add level
        level = str(user.level)
        font = Font.poppins(size=20)
        editor.text((350, 90), level, font=font, color="white")

        #add xp
        xp = str(user.xp)
        font = Font.poppins(size=20)
        editor.text((530, 91), xp, font=font, color="white")

        #add roles

        #add questions answered
        qa = str(user.qotd.total_questions)
        font = Font.poppins(size=20)
        editor.text((255, 322), qa, font=font, color="white")

        #add correct
        correct = str(user.qotd.correct)
        font = Font.poppins(size=20)
        editor.text((120, 370), correct, font=font, color="white")

        #add points
        points = str(user.qotd.points)
        font = Font.poppins(size=20)
        editor.text((255, 370), points, font=font, color="white")

        #add wins
        wins = str(user.qotd.wins)
        font = Font.poppins(size=20)
        editor.text((120, 416), wins, font=font, color="white")

        #add top 3
        top3 = str(user.qotd.top_3)
        font = Font.poppins(size=20)
        editor.text((255, 416), top3, font=font, color="white")

        #add avatar
        avatar_url = member.display_avatar.url  # always works, even if no custom avatar
        avatar = await load_image_async(avatar_url)  # EasyPIL helper to fetch and load
        avatar_editor = Editor(avatar).resize((175, 175)).circle_image()  # crop circle

        editor.paste(avatar_editor, (30, 60))





        #endregion

        buffer = io.BytesIO()
        editor.image.save(buffer, format="PNG")
        buffer.seek(0)

        file = discord.File(fp=buffer, filename="modified_image.png")

        return file

    except Exception as e:
        print(f"send_usercard error(function): {e}")
#endregion
#region  chunk_list
def chunk_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
#endregion

#event functions-----------------------------
#region  load_player
async def load_player(client, user_id, guild_id):
    try:
        guild = client.get_guild(guild_id)
        member = await guild.fetch_member(user_id)
        await create_player(client, user_id, member.display_name, guild_id)
        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT data FROM players WHERE user_id = ? AND guild = ?", (user_id, guild_id))
            row = await cursor.fetchone()
        if row:
            data = json.loads(row[0])
            return objects.Player.from_dict(client, data)
        return None
    except Exception as e:
        print(f"load_player error: {e}")
#endregion
#region  create_player
async def create_player(client, user_id, display_name, guild_id):
    try:
        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT data FROM players WHERE user_id = ? AND guild =?", (user_id, guild_id))
            user = await cursor.fetchone()
            if user is None:
                new_user = objects.Player(client, user_id, display_name, guild_id)
                await new_user.save()
            else:
                return
    except Exception as e:
        print(f"create_player error: {e}")
#endregion
#region  event_message
async def event_message(client, react_data):
    message_id = react_data.get('message_id')
    user_id = react_data.get('user_id')
    emoji = react_data.get('emoji')
    guild_id = react_data.get('guild_id')
    guild = client.get_guild(guild_id)
    member = guild.get_member(user_id)
    emoji = str(emoji)

    async with client.db.cursor() as cursor:
        await cursor.execute("SELECT role FROM event WHERE message_id = ? AND emoji = ?", (message_id, emoji,))
        role_id = await cursor.fetchone()
        if role_id is None:
            return
        else:
            role_id = role_id[0]
            role = discord.utils.get(guild.roles, id=role_id)
            await member.add_roles(role)
            await create_player(client, user_id, member.display_name, guild_id)
#endregion
#region  add_event_react
async def add_event_react(client, message_id, role, emoji, channel):
        try:
            message_id = int(message_id)
            role = int(role)
            async with client.db.cursor() as cursor:
                await cursor.execute("INSERT INTO event (message_id, role, emoji) VALUES (?, ?, ?)", (message_id, role, emoji,))
                await client.db.commit()

                message = await channel.fetch_message(message_id)
                await message.add_reaction(emoji)
        except Exception as e:
            print(f"add_event_react error(function): {e}")
#endregion
#region  log_drop
async def log_drop(client, player, new_points, message, tier):
    updated = False

    #check if drop is logged
    channel = client.get_channel(config.EVENT_CHANNEL)

    if str(message.id) in player.drops.log:
        old_points = player.drops.log[str(message.id)]["points"]
        old_drop_id = player.drops.log[str(message.id)]["drop_id"]
        old_drop_tier = player.drops.log[str(message.id)]["tier"]
        try:
            old_message = await channel.fetch_message(old_drop_id)
        except NotFound:
            old_message = None  # message was deleted
        if old_message is None:
            pass
        else:
            await old_message.edit(content=f"<:gods_event:1413469035777097758> | <@{player.id}> has contributed **{new_points}** Points to the Altar! -> {message.jump_url}")
        updated = True

    #log the drop
    if updated:
        player.drops.log[str(message.id)]["points"] -= old_points
        player.points -= old_points
        player.drops.log[str(message.id)]["points"] += new_points
        player.points += new_points
        player.drops.log[str(message.id)]["tier"] = tier
        current_value = getattr(player.drops, old_drop_tier)
        setattr(player.drops, tier, current_value - 1)

        new_value = getattr(player.drops, tier)
        setattr(player.drops, tier, new_value + 1)
    else:
        new_drop_message = await post_drop(channel, new_points, player.id, message)
        player.drops.log[message.id] = {"points": new_points, "drop_id": new_drop_message.id, "tier": tier}
        player.points += new_points
        new_value = getattr(player.drops, tier)
        setattr(player.drops, tier, new_value + 1)

        #add reaction to confirm drop is logged
        emoji = "✅"
        await message.add_reaction(emoji)
    await player.save()
#endregion
#region  post_drop
async def post_drop(channel, new_points, player_id, message):
    new_message = await channel.send(f"<:gods_event:1413469035777097758> | <@{player_id}> has contributed **{new_points}** Points to the Altar! -> {message.jump_url}")

    messages = []
    async for message in channel.history(limit=100, oldest_first=True):
        messages.append(message)

    if len(messages) > 16:
        purged = await channel.fetch_message(messages[1].id)
        await purged.delete()

    #update main bar view  (function possibly)----------------------------------------------------------------------------

    return new_message
#endregion


