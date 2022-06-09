import json
import telebot
from telebot import types

from config import TOKEN, logger
from main import check_news


bot = telebot.TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    btn_1 = types.KeyboardButton(text="Latest 5 news")
    btn_2 = types.KeyboardButton(text="Fresh news")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_1).add(btn_2)

    bot.reply_to(message, text='News feed', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_five_news(message: telebot.types.Message):
    logger.info('Latest 5 news')

    with open("news_dict.json", encoding='utf-8') as file:
        news_dict = json.load(file)
    if message.text == 'Latest 5 news':
        for k, v in sorted(news_dict.items())[-5:]:
            news = f"<b>{v['article_data_time']}</b>\n" \
                   f"<u>{v['article_title']}</u>\n" \
                   f"{v['article_url']}"

            bot.reply_to(message, news)


@bot.message_handler(content_types=['text'])
def get_fresh_news(message: telebot.types.Message):
    logger.info('Fresh news')

    fresh_news = check_news()
    if message.text == 'Fresh news':
        if len(fresh_news) >= 1:
            for k, v in sorted(fresh_news.items()):
                news = f"{v['article_data_time']}" \
                       f"{v['article_title']} " \
                       f"{v['article_url']}"

                bot.reply_to(message, news)
        else:
            bot.reply_to(message, text='No fresh news yet')


if __name__ == '__main__':
    bot.polling(none_stop=True)