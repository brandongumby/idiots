from bosses.vorago import vmenu, hmvmenu
from bosses.raids import raidsmenu
from bosses.aod import aodmenu, aod5menu, aod8menu
from bosses.vorkath import vorkmenu
from bosses.rots import rotsmenu
from bosses.kerapac import keramenu
from bosses.solak import solakmenu
from bosses.croesus import cromenu
from bosses.zammy import zammymenu
from bosses.sanctum import sormenu
from bosses.gate import goemenu
from bosses.eds import edsmenu
from bosses.amascut import amascutmenu, hmamascutmenu
from util import myviews, config
import json


async def create_views(client, TaskClass):
    try:
        view_list = [
            myviews.TeamformView(client),
            aodmenu.AodMenu(client, 2),
            aod5menu.Aod5Menu(client, 2),
            aod8menu.Aod8Menu(client, 2),
            sormenu.SorMenu(client, 11),
            cromenu.CroeMenu(client, 4),
            keramenu.KeraMenu(client, 5),
            raidsmenu.RaidsMenu(client, 6),
            rotsmenu.RotsMenu(client, 7),
            solakmenu.SolakMenu(client, 8),
            vmenu.VoragoMenu(client, 1),
            hmvmenu.HMVoragoMenu(client, 3),
            vorkmenu.VorkMenu(client, 9),
            zammymenu.ZammyMenu(client, 10),
            goemenu.GoeMenu(client, 12),
            edsmenu.EdsMenu(client, 13),
            amascutmenu.AmasMenu(client, 14),
            hmamascutmenu.HMAmasMenu(client, 14),
            myviews.CloseMenu(),
            myviews.CreateTicket(client),
            myviews.TicketSettings(client),
            myviews.CreatePOFTicket(client),
            myviews.POFTicketSettings(client),
            myviews.POFLendView(client),
            myviews.GiveawayEnter(client, TaskClass),
            myviews.GiveawayEnd(client, TaskClass),
        ]

        async with client.db.cursor() as cursor:
            await cursor.execute("SELECT tagged, correct, difficulty, results, answered FROM qotd WHERE guild = ?", (config.GUILD_ID,))
            row = await cursor.fetchone()

            if row[0]:
                tagged = json.loads(row[0])
                correct = json.loads(row[1])
                difficulty = json.loads(row[2])
                if row[3]:
                    results = json.loads(row[3])
                else:
                    results = {'🇦': 0, '🇧': 0, '🇨': 0, '🇩': 0,}
                if row[4]:
                    answered = json.loads(row[4])
                else:
                    answered = []
                view_list.append(myviews.QotdView(client, tagged, correct, difficulty, results, answered))

        return view_list
    except Exception as e:
        print(f"create_views error(persistence): {e}")