import telebot

from BackendRu import Grammar

bot = telebot.TeleBot('5870665472:AAEy76MfCreoMYN1PQRN5DTyB3R_JTT31ps')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Приветствую вас ,{message.from_user.first_name}. Я могу проверить слово "
                                      f"на написание суффиксов в инфинитиве, где присутствуют сомнения в написании.\n"
                                      f"Для проверки написания слова, необходимо ввести слово"
                                      f" с нижним подчёркиванием в месте сомнения в написании. "
                                      f"\nПримеры:  стели_ть, бег_ть и т.д.")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    a = Grammar(message.text.lower(), ['и','а','я','е','ы','о'])
    bot.send_message(message.chat.id, a.find_the_right_word())


bot.infinity_polling()
