from found import SendBot
from search import Search
import requests
from Yui.key import telegram_token

TOKEN = telegram_token


def telegram_bot_send_text(bot_message, chat_id):
    bot_chat_id = str(chat_id)
    send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


bot = SendBot()
archive_list = bot.create_profile()
search_list = [Search(link["manga"]) for link in archive_list]
id_list = [link["chat_id"] for link in archive_list]
link_list = [link["manga"] for link in archive_list]
chapter = [status.search_ep() for status in search_list]
i = -1
no_new_chapter = 0
for link in chapter:
    i += 1
    user = id_list[i]
    if link["is_new"]:
        message = (f"There's a new chapter: {link['chapter_num']} "
                   f"named: {link['chapter_name']}, link: {link_list[chapter.index(link)]}")
        telegram_bot_send_text(bot_message=message, chat_id=user.strip())
        print(message, user)
    else:
        print("There is no new chapter")
        no_new_chapter += 1
        if no_new_chapter == len(chapter):
            telegram_bot_send_text(bot_message="There's no new chapter today", chat_id=user.strip())
for search in search_list:
    search.close_tabs()
