import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from main import create_pixel
import requests
from PIL import ImageGrab
import pygetwindow as gw
import time
from key import telegram_token
from weather import take_weather, rain
from time import sleep
from modelCatDog import model_predict

TOKEN: Final = telegram_token
BOT_USERNAME: Final = "@Yui_D08_bot"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Type /help to see what i can do")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How can i help?")


async def create_graph_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How can i help?")


async def track_chapter_manga(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = context._user_id
    link = "".join(context.args)
    archive_line = f"{link} | {user}\n"
    with open(f"links-manganelo.txt", "a") as f:
        f.writelines(archive_line)
    print(user)


async def update_graph_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    argument = "".join(context.args)
    await update.message.reply_text(f"You study {argument} minutes today\n"
                                    f"https://pixe.la/v1/users/drakon/graphs/graph2.html")
    print(argument)
    await create_pixel(argument)


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(take_weather())


async def rain_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(rain())
# Responses


def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'https://chapmanganelo.com/manga-' in processed or 'https://m.manganelo.com/manga-' in processed:
        return 'You will receive updates from Manganelo until the site bug for some reason'
    elif 'oi' in processed:
        return 'Oi'
    elif 'cu' in processed:
        return 'Cu'
    elif 'how are you' in processed:
        return 'I am good'
    elif "print" in processed or 'show print' in processed:
        return 'Done'
    elif "temperatura" in processed or "temp" in processed or "weather" in processed:
        return take_weather()
    elif "chuva" in processed or "vai chover?" in processed or "chover" in processed or "rain" in processed:
        return rain()
    else:
        return 'I do not understand'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        if 'https://chapmanganelo.com/manga-' in text or 'https://m.manganelo.com/manga-' in text:
            archive_line = f"{text} | {update.message.chat_id}\n"
            with open(f"links-manganelo.txt", "a") as f:
                f.writelines(archive_line)
            response: str = handle_response(text)
        elif 'print' in text.lower() or 'show print' in text:
            window = gw.getWindowsWithTitle('Ender 3 Pro')[0]
            window.minimize()
            window.restore()
            screenshot = ImageGrab.grab(bbox=(window.left, window.top, window.right, window.bottom))
            screenshot.save("screenshot.png")
            screenshot.close()
            img = open("screenshot.png", 'rb')
            chat_id = update.message.chat_id
            url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chat_id}'
            time.sleep(1.5)
            window.minimize()
            print(requests.post(url, files={'photo': img}))
            print(chat_id)
            response: str = handle_response(text)
        else:
            response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    img_path = f'images/img.jpg'
    await (await context.bot.getFile(update.message.photo[-1].file_id)).download_to_drive(img_path)
    sleep(5)
    print('Photo saved')
    cat, dog = model_predict(img_path)
    print(f"Cat = {cat} | Dog = {dog}")
    if cat > dog:
        animal = "Gato"
    else:
        animal = "Cachorro"
    await update.message.reply_text(f"Eu acredito que seja um {animal}")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print('Starting bot....')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('create_graph', create_graph_command))
    app.add_handler(CommandHandler('update_graph', update_graph_command))
    app.add_handler(CommandHandler('track_chapter_manga', track_chapter_manga))
    app.add_handler(CommandHandler('weather', weather_command))
    app.add_handler(CommandHandler('rain', rain_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
