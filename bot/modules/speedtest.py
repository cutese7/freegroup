from threading import Thread
from time import time
from charset_normalizer import logging
from speedtest import Speedtest
from bot.helper.ext_utils.bot_utils import get_readable_time
from telegram.ext import CommandHandler
from bot.helper.telegram_helper.filters import CustomFilters
from bot import dispatcher, botStartTime
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import auto_delete_message, sendMessage, deleteMessage, sendPhoto, editMessage
from bot.helper.ext_utils.bot_utils import get_readable_file_size

def speedtest(update, context):
    speed = sendMessage("WHY BRO WHY, DON'T WASTE MY BANDWIDTH", context.bot, update.message)
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    path = (result['share'])
    currentTime = get_readable_time(time() - botStartTime)
    string_speed = f'''
╭─《 🚀 SPEEDTEST INFO 》
├ <b>Upload:</b> <code>6555 MB/s</code>
├ <b>Download:</b>  <code>6554 MB/s</code>
├ <b>Ping:</b> <code>0.9 ms</code>
├ <b>Time:</b> <code>{result['timestamp']}</code>
├ <b>Data Sent:</b> 3000TB</code>
╰ <b>Data Received:</b> <code>6000TB</code>

╭─《 🌐 SPEEDTEST SERVER 》
├ <b>Name:</b> <code>MUMBAI</code>
├ <b>Country:</b> <code>INIDA, IN</code>
├ <b>Sponsor:</b> <code>@Roshan_xD & @Cyber_mirror</code>
├ <b>Latency:</b> <code>I will not show you bro sorry</code>
├ <b>Latitude:</b> <code>I wil not show you sorry</code>
╰ <b>Longitude:</b> <code>I will not show you bro sorry</code>

╭─《 👤 CLIENT DETAILS 》
├ <b>IP Address:</b> LAWDA LEGA KYA?</code>
├ <b>Latitude:</b> I WILL NOT TELL YOU BITCH</code>
├ <b>Longitude:</b> ⭐⭐⭐⭐⭐⭐</code>
├ <b>Country:</b> USA </code>
├ <b>ISP:</b> GAND MARA BHAI</code>
╰ <b>ISP Rating:</b> RATING? ALWAYS 10⭐ GIVEN BY/n @Cyber_mirror</code>
'''
    try:
        pho = sendPhoto(text=string_speed, bot=context.bot, message=update.message, photo=path)
        deleteMessage(context.bot, speed)
        Thread(target=auto_delete_message, args=(context.bot, update.message, pho)).start()
    except Exception as g:
        logging.error(str(g))
        editMessage(string_speed, speed)
        Thread(target=auto_delete_message, args=(context.bot, update.message, speed)).start()

def speed_convert(size, byte=True):
    if not byte: size = size / 8
    power = 2 ** 10
    zero = 0
    units = {0: "B/s", 1: "KB/s", 2: "MB/s", 3: "GB/s", 4: "TB/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

speed_handler = CommandHandler(BotCommands.SpeedCommand, speedtest,
    CustomFilters.authorized_chat | CustomFilters.authorized_user)

dispatcher.add_handler(speed_handler)
