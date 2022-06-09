import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):

    bot.reply_to(message, text='News feed')


if __name__ == '__main__':
    bot.polling(none_stop=True)