import json
import telebot

from config import TOKEN


bot = telebot.TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):

    bot.reply_to(message, text='News feed')


@bot.message_handler(commands=['last_five'])
def get_five_news(message: telebot.types.Message):
    with open("news_dict.json", encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"<b>{v['article_data_time']}</b>\n" \
               f"<u>{v['article_title']}</u>\n" \
               f"{v['article_url']}"

        bot.reply_to(message, news)


if __name__ == '__main__':
    bot.polling(none_stop=True)