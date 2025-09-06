#region  imports
# Standard library
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# custom modules
from util import functions

#endregion



scheduler = AsyncIOScheduler()

async def monthly_task(client):
    await functions.qotd_gratz(client)

async def daily_task(client):
    await functions.send_qotd(client)
    #await functions.DemonSpotlight(client)

def setup_scheduler(client):
    scheduler.add_job(monthly_task, CronTrigger(day=1, hour=11, minute=0, timezone=pytz.utc), args=[client])
    scheduler.add_job(daily_task, CronTrigger(hour=11, minute=0, timezone=pytz.utc), args=[client])
    scheduler.start()


    