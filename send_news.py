from telebot import TeleBot
import time
from random import choice
import logging

from news_sources import WorldNYTimesNewsSource, USANYTimesNewsSource

from utils.alerting import handle_exception

logging.basicConfig(level=logging.INFO)


bot = TeleBot(
    token='5860842320:AAEfKtZppebM_04-4yspPqntUhZlmZCv2kg',
    parse_mode='html',
    disable_web_page_preview=True,
)
news_to_post = 10
sources = [
    WorldNYTimesNewsSource(),
    USANYTimesNewsSource(),
]


if __name__ == '__main__':
    logging.info(f'News to post: {news_to_post}')

    try:
        while news_to_post:

            source = WorldNYTimesNewsSource()
            news = source.get_one_news()
            if not news:
                print(news_to_post)
                news_to_post -= 1
                continue

            photo = source.create_mem_from_photo(news=news)
            caption = source.constract_caption(news)

            bot.send_photo(
                chat_id='-1001965039048',
                photo=open(photo, 'rb'),
                caption=caption,
            )
            logging.info(f'News {news.title} was sent')
            photo.unlink()
            time.sleep(25)
            news_to_post -= 1
    except Exception as e:
        handle_exception(bot=bot, e=e)