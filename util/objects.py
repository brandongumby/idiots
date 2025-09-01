from util import functions
import json


class User:
    def __init__(self, client, name, user_id, guild_id, roles: list):
        self.client = client
        self.name = name
        self.id = user_id
        self.guild = guild_id
        self.level = 0
        self.xp = 0
        self.roles = roles
        self.messages = 0
        self.qotd = self.Qotd()
        self.achievements = self.Achievements()

    class Qotd:
        def __init__(self):
            self.points = 0
            self.correct = 0
            self.wins = 0
            self.top_3 = 0
            self.total_questions = 0

    class Achievements:
        def __init__(self):
            self.tier = ""
            self.skilling = self.Skilling()
            self.combat = self.Combat()
            self.clan = self.Clan()
            self.drops = self.Drops()
            self.completed = []

        def reset(self):
            self.tier = ""
            self.completed = []
            for category in (self.skilling, self.combat, self.clan, self.drops):
                category.tasks = 0
                category.points = 0
                if hasattr(category, "logged"):
                    category.logged = []  # only exists in Drops

        @property
        def total_tasks(self):
            return self.skilling.tasks + self.combat.tasks + self.clan.tasks + self.drops.tasks
        
        @property
        def total(self):
            return self.skilling.points + self.combat.points + self.clan.points + self.drops.points
        def __int__(self):
            return self.total
        def __str__(self):
            return str(self.total)
        
        class Skilling:
            def __init__(self):
                self.tasks = 0
                self.points = 0
            
        class Combat:
            def __init__(self):
                self.tasks = 0
                self.points = 0

        class Clan:
            def __init__(self):
                self.tasks = 0
                self.points = 0

        class Drops:
            def __init__(self):
                self.tasks = 0
                self.points = 0
                self.logged = []

#region  --- serialization ---
    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "guild": self.guild,
            "level": self.level,
            "xp": self.xp,
            "roles": self.roles,
            "messages": self.messages,
            "qotd": vars(self.qotd),
            "achievements": {
                "tier": self.achievements.tier,
                "skilling": vars(self.achievements.skilling),
                "combat": vars(self.achievements.combat),
                "clan": vars(self.achievements.clan),
                "drops": vars(self.achievements.drops),
                "completed": self.achievements.completed,
            }
        }

    @classmethod
    def from_dict(cls, client, data: dict):
        user = cls(
            client,
            data.get("name", "Unknown"),
            data["id"],
            data["guild"],
            data.get("roles", []),
        )
        user.level = data.get("level", 0)
        user.xp = data.get("xp", 0)
        user.messages = data.get("messages", 0)

        # Qotd (gracefully handle missing fields)
        qotd_data = data.get("qotd", {})
        user.qotd.points = qotd_data.get("points", 0)
        user.qotd.correct = qotd_data.get("correct", 0)
        user.qotd.wins = qotd_data.get("wins", 0)
        user.qotd.top_3 = qotd_data.get("top_3", 0)
        user.qotd.total_questions = qotd_data.get("total_questions", 0)

        # Achievements
        ach = data.get("achievements", {})
        for category in ["skilling", "combat", "clan", "drops"]:
            cat_data = ach.get(category, {})
            getattr(user.achievements, category).tasks = cat_data.get("tasks", 0)
            getattr(user.achievements, category).points = cat_data.get("points", 0)
            if category == "drops":
                getattr(user.achievements, category).logged = cat_data.get("logged", [])

        user.achievements.completed = ach.get("completed", [])
        user.achievements.tier = ach.get("tier", "")
        return user
        
    async def save(self):
        try:
            data = json.dumps(self.to_dict())
            async with self.client.db.cursor() as cursor:
                await cursor.execute("""
                    INSERT INTO users (user_id, guild, data)
                    VALUES (?, ?, ?)
                    ON CONFLICT(user_id, guild) DO UPDATE SET data=excluded.data
                """, (self.id, self.guild, data))
            await self.client.db.commit()
        except Exception as e:
            print(f"save_user error(objects.py): {e}")


    #--->  CREATE UNIQUE INDEX idx_user_guild ON users(user_id, guild);
#endregion

