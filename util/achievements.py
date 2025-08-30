

achievements = [
    {"name": "120 all", "points": 50, "tasks": 1, "cat": "skilling"},
    {"name": "Maxed", "points": 25, "tasks": 1, "cat": "skilling"},
    {"name": "Completionist", "points": 50, "tasks": 1, "cat": "skilling"},
    {"name": "Trim Comp", "points": 75, "tasks": 1, "cat": "skilling"},
    {"name": "5.8b XP", "points": 50, "tasks": 1, "cat": "skilling"},
    {"name": "Master of All", "points": 100, "tasks": 1, "cat": "skilling"},
    {"name": "Nex: Angel of Death Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Arch-Glacor Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Arraxi Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Croesus Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "ED1 Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "ED2 Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "ED3 Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "ED4 Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Kerapac Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Kalphite King Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Nex Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Raksha Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Rasial Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Solak Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Telos Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Vorago Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Vorkath Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "TzKal-Zuk Mastery", "points": 25, "tasks": 1, "cat": "combat"},
    {"name": "Tick Perfect", "points": 50, "tasks": 1, "cat": "combat"},
    {"name": "Elitest Dungeon", "points": 50, "tasks": 1, "cat": "combat"},
    {"name": "Animaster", "points": 50, "tasks": 1, "cat": "combat"},
    {"name": "Who Needs Friends?", "points": 50, "tasks": 1, "cat": "combat"},
    {"name": "4k Telos", "points": 75, "tasks": 1, "cat": "combat"},
    {"name": "4k Glacor", "points": 75, "tasks": 1, "cat": "combat"},
    {"name": "4k Zamorak (solo)", "points": 75, "tasks": 1, "cat": "combat"},
    {"name": "4k Zamorak (group)", "points": 75, "tasks": 1, "cat": "combat"},
    {"name": "2k Amascut", "points": 75, "tasks": 1, "cat": "combat"},
    {"name": "Golden Praesul", "points": 75, "tasks": 1, "cat": "combat"},
    {"name": "Insane Final Boss", "points": 100, "tasks": 1, "cat": "combat"},
    {"name": "Golden Reaper", "points": 100, "tasks": 1, "cat": "combat"},
    {"name": "Ultimate Slayer", "points": 100, "tasks": 1, "cat": "combat"},
    {"name": "Winning a clan event", "points": 100, "tasks": 1, "cat": "clan"}
]

def fetch(target, cat=None, default="name"):
    return [a.get(target, default) for a in achievements if cat is None or a.get("cat") == cat]

def fetch_uncomplete(completed_list):
    ach_list = [a.get("name") for a in achievements]

    result = [x for x in ach_list if x not in completed_list]
    return result