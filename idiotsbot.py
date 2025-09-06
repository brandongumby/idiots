#region  imports
# Standard library
import asyncio

# Third-party libraries
import discord
from discord import app_commands
import aiosqlite

# custom modules
from util import config, functions, persistence, commands, schedules
#endregion


BOT_TOKEN = config.BOT_TOKEN


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
        self.added = False

#region on_ready
    async def on_ready(self):
            await self.wait_until_ready()
            self.db = await aiosqlite.connect('idiotsdata.db') #connecting to database
            await functions.set_activity(self)
            schedules.setup_scheduler(client)

            if not self.synced:
                synced = await tree.sync()
                print(f"Synced {len(synced)} command(s)")
                self.synced = True

            if not self.added:
                views = await persistence.create_views(client, TaskClass)
                for view in views:
                    self.add_view(view)
                self.added = True

            print(f'{client.user} is online!')

            async with self.db.cursor() as cursor:
                # Database for events
                await cursor.execute("CREATE TABLE IF NOT EXISTS players (user_id INTEGER, data TEXT, guild INTEGER, UNIQUE(user_id, guild))")
                await cursor.execute("CREATE TABLE IF NOT EXISTS event (message_id INTEGER, role INTEGER, emoji STRING)")
                await cursor.execute("CREATE TABLE IF NOT EXISTS event_progress (total INTEGER, guild INTEGER)")

                # User data
                await cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, data TEXT, guild INTEGER, qotd_points INTEGER, UNIQUE(user_id, guild))")

                # System databases
                await cursor.execute("CREATE TABLE IF NOT EXISTS tickets (user INTEGER, guild INTEGER, status STRING)")
                await cursor.execute("CREATE TABLE IF NOT EXISTS voice_channels (channel_id INTEGER, guild INTEGER)")
                await cursor.execute("CREATE TABLE IF NOT EXISTS react (message_id INTEGER, role INTEGER, emoji STRING)")
                await cursor.execute("CREATE TABLE IF NOT EXISTS giveaways (message_id INTEGER, host INTEGER, participants TEXT, prize STRING, end_time INTEGER, description STRING, finished STRING, winners INTEGER)")
                await cursor.execute("CREATE TABLE IF NOT EXISTS messages (user INTEGER, username STRING, message_id INTEGER, guild INTEGER, content STRING, created_at INTEGER)")
                await cursor.execute("CREATE TABLE IF NOT EXISTS animals (animal STRING, guild INTEGER, breed1 STRING, traita1 STRING, traita2 STRING, traita3 STRING, breed2 STRING, traitb1 STRING, traitb2 STRING, traitb3 STRING, owner STRING, lender STRING)")
                
                # Question of the day no-repeat and persistence databases
                await cursor.execute("CREATE TABLE IF NOT EXISTS questions (question STRING, guild INTEGER)")
                await cursor.execute("CREATE TABLE IF NOT EXISTS qotd (message_id STRING, guild INTEGER, tagged TEXT, correct TEXT, difficulty TEXT, results TEXT, answered TEXT, gratz_message_id STRING)")
                await client.db.commit()

            await functions.StartTask(TaskClass)

    async def close(self):
            if hasattr(self, 'db') and self.db is not None:
                await self.db.close()
            await super().close()
#endregion

client = aclient()
tree = app_commands.CommandTree(client)


#region on_message (level and xp gain)
@client.event
async def on_message(message): 
    try:     
        if message.author.bot:
            return
        await functions.create_acc(client, message.author.id, message.author.display_name, message.guild.id)
        if message.guild.id == config.GUILD_ID:
            message_time_unix = int(message.created_at.timestamp())
            message_data = {"message_id": message.id, "content": message.content,"guild": message.guild.id, "user_id": message.author.id, "username": message.author.name, "created_at": message_time_unix}
            
            roles = message.author.roles
            await functions.store_user_roles(client, message.author.id, message.guild.id)
            
            await functions.cache_message(client, message_data)
            await functions.PurgeOldMessage(client)
            await functions.gain_xp(client, message.author.id, message.guild.id)

            user = await functions.load_user(client, message.author.id, message.guild.id)
            user.messages += 1
            await user.save()
        else:
            return
    except Exception as e:
        print(f"on_message(message) error: {e}")
#endregion

#region on_member_join
@client.event
async def on_member_join(member):
    try:
        await functions.create_acc(client, member.id, member.display_name, member.guild.id)

        if member.guild.id == config.GUILD_ID:
            logs_channel = client.get_channel(config.LOGS_CHANNEL)
            role = discord.utils.get(member.guild.roles, name=config.GUEST_ROLE)
            channel = client.get_channel(config.GENERAL_CHANNEL)
            welcome_message = (f"Welcome <@{member.id}>, feel free to self assign any roles at <#{config.SELF_ASSIGN_CHANNEL}> and check out our rules <#{config.RULES_CHANNEL}>. If you have any questions don't hesitate to ask in here or one of our great Leadership members!")

            await member.add_roles(role)
            await channel.send(welcome_message)

            creation_time = await functions.get_time(str(member.created_at))

            joinembed = discord.Embed(title="Member Joined!", description=f"{member.name}", color=0x20fc03)
            joinembed.set_thumbnail(url=member.display_avatar.url)
            joinembed.add_field(name=f"", value=f"{member.mention} joined\nNew member count is {member.guild.member_count}.")
            joinembed.add_field(name="Account Created:", value=f"<t:{creation_time}:F>\n<t:{creation_time}:R>", inline=False)
            await logs_channel.send(embed=joinembed)
        else:
            return
    except Exception as e:
        print(f"on_member_join(member) error: {e}")
#endregion

#region on member leave
@client.event
async def on_raw_member_remove(payload):
    try:
        if payload.user.bot:
            return
        if payload.guild_id == config.GUILD_ID:
            logs_channel = client.get_channel(config.LOGS_CHANNEL)
            user = await functions.load_user(client, payload.user.id, payload.guild_id)
            role_mentions = [f"<@&{role.id}>" for role in payload.user.guild.roles if role.id in user.roles]

            creation_time = await functions.get_time(str(payload.user.created_at))
            joined_at_time = await functions.get_time(str(payload.user.joined_at))

            joinembed = discord.Embed(title="Member Left!", description=f"{payload.user.name}", color=0x800000)
            joinembed.set_thumbnail(url=payload.user.display_avatar.url)
            joinembed.add_field(name=f"", value=f"{payload.user.mention} Left\nNew member count is {payload.user.guild.member_count}.")
            joinembed.add_field(name="Server Nickname:", value=f"{user.name}", inline=False)
            joinembed.add_field(name="Account Created:", value=f"<t:{creation_time}:R>", inline=False)
            joinembed.add_field(name="Joined Idiots:", value=f"<t:{joined_at_time}:R>", inline=False)
            joinembed.add_field(name="Roles:", value=f"{', '.join(role_mentions)}", inline=False)
            await logs_channel.send(embed=joinembed)
        else:
            return
    except Exception as e:
        print(f"on_raw_member_remove error: {e}")
#endregion

#region on_member_update
@client.event
async def on_member_update(before, after):
    try:
        await functions.create_acc(client, before.id, before.display_name, before.guild.id)
        if after.guild.id == config.GUILD_ID:
            if before.roles != after.roles:
                await functions.store_user_roles(client, before.id, after.guild.id)
            logs_channel = client.get_channel(config.LOGS_CHANNEL)
        
            if before.display_avatar != after.display_avatar:
                avatar_change_embed = discord.Embed( title="Member Avatar Updated", description=f"{after.mention} has updated their avatar!", color=0x037ffc)
                avatar_change_embed.add_field(name="New Avatar", value=f"[New Avatar]({after.display_avatar.url})", inline=False)
                avatar_change_embed.set_thumbnail(url=after.display_avatar.url)
                await logs_channel.send(embed=avatar_change_embed)
        else:
            return
    except Exception as e:
        print(f"on_member_update error: {e}")
#endregion

#region on message delete
@client.event
async def on_raw_message_delete(payload):
    try:
        if payload.guild_id == config.GUILD_ID:
            message_id = payload.message_id
            channel_id = payload.channel_id

            if payload.channel_id in config.IGNORE_LOGGING:
                return
            
            message_data = {"message_id": message_id, "channel_id": channel_id}
            await functions.delete_message(client, message_data)
        else:
            return
    except Exception as e:
        print(f"on_raw_message_delete error: {e}")
#endregion

#region on message edit
@client.event
async def on_raw_message_edit(payload):
    try:
        if payload.guild_id == config.GUILD_ID:
            if payload.channel_id in config.IGNORE_LOGGING:
                return

            author_is_bot = payload.data.get('author', {}).get('bot', False)
            if author_is_bot:
                return
            
            message_data = {"message_id": {payload.data['id']}, "content": {payload.data['content']}, "user_id": {payload.data['author']['id']}, "username": {payload.data['author']['username']},}
            await functions.edit_cache_message(client, message_data)
        else:
            return
    except Exception as e:
        print(f"on_raw_message_edit error: {e}")
#endregion

#region reaction roles add
@client.event
async def on_raw_reaction_add(payload):
    try:
        author_is_bot = payload.member.bot
        if author_is_bot:
            return
        if payload.member:
            display_name = payload.member.display_name
        else:
            guild = client.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            display_name = member.display_name
        await functions.create_acc(client, payload.member.id, display_name, payload.member.guild.id)
        message_id = payload.message_id
        user_id = payload.user_id
        emoji = payload.emoji
        guild_id = payload.member.guild.id

        channel = client.get_channel(payload.channel_id)
        if channel is None:
            channel = await client.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        message_author = await functions.load_user(client, message.author.id, payload.guild_id)
        message_author.achievements.clan.points += 1
        await message_author.save()

        react_data = {"message_id": message_id, "user_id": user_id, "emoji": emoji, "guild_id": guild_id}

        await functions.add_react_role(client, react_data)
        await functions.event_message(client, react_data)
    except Exception as e:
        print(f"on_raw_reaction_add error: {e}")
#endregion

#region reaction roles remove
@client.event
async def on_raw_reaction_remove(payload):
    try:
        message_id = payload.message_id
        user_id = payload.user_id
        emoji = payload.emoji
        guild_id = payload.guild_id

        react_data = {"message_id": message_id, "user_id": user_id, "emoji": emoji, "guild_id": guild_id}

        await functions.remove_react_role(client, react_data)
    except Exception as e:
        print(f"on_raw_reaction_remove error: {e}")
#endregion

#region create temp voice
@client.event
async def on_voice_state_update(member, before, after):
    try:
        guild = member.guild
        category = discord.utils.get(guild.categories, id=config.VOICE_CATEGORY_ID)
        channel_name = (f"{member.display_name}'s Channel")
        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT channel_id FROM voice_channels WHERE guild = ?", (member.guild.id,))
            rows = await cursor.fetchall()
            channel_ids = [row[0] for row in rows]

            if before.channel and before.channel.id in channel_ids:

                if len(before.channel.members) == 0:
                    await before.channel.delete()
                    await cursor.execute("DELETE FROM voice_channels WHERE guild = ? AND channel_id = ?", (member.guild.id, before.channel.id,))

                    await client.db.commit()
            else:
                pass

            if after.channel and after.channel.id == config.VOICE_CHANNEL:
                new_channel = await guild.create_voice_channel(name=channel_name, category=category)
                await cursor.execute("INSERT INTO voice_channels (channel_id, guild) VALUES (?, ?)", (new_channel.id, member.guild.id,))
                await client.db.commit()

                await member.move_to(new_channel)
    except Exception as e:
        print(f"on_voice_state_update error: {e}")
#endregion


class TaskClass:
    def __init__(self, client):
        self.client = client
        self.give = None

    def start_task(self):
        try:
            self.give = self.client.loop.create_task(functions.fetch_giveaways(self.client, self))
        except Exception as e:
            print(f"start_task error: {e}")


    def give_not_done(self):
        try:
            if self.give is None:
                return False  # No task has been started
            return not self.give.done()
        except Exception as e:
            print(f"give_not_done error: {e}")
    
TaskClass = TaskClass(client)

commands.load_commands(tree, client, TaskClass)


async def main():
    async with client:
        await client.start(BOT_TOKEN)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Received exit signal, shutting down...")
