import os
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def send_power_alert():
    bot.send_message(chat_id=CHAT_ID, text="⚡ هشدار برق امروز: ممکنه قطع بشه!")

scheduler = BlockingScheduler()
scheduler.add_job(send_power_alert, 'cron', hour=9)
scheduler.start()
