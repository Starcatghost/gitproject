import telebot
import base_bot
import app_api

bot = telebot.TeleBot(base_bot.TOKEN)
print('bot api created')

@bot.message_handler(commands=['api'])
def call_api(message):
    msg = bot.send_message(message.chat.id, text= 'ای دی فیلم مورد نظر(250-10)را وارد کنید')
    bot.register_next_step_handler(msg, get_movie_info )


def get_movie_info(message):
    movie_id = eval(message.text)
    if movie_id > 250:
        bot.send_message(message.chat.id, text= 'ایدی فیلم باید در محدوده مشخصی باشد')
    else: 
        result = app_api.get_movie_info_by_id(movie_id)

        bot.send_message(message.chat.id, f'{result[0]} - {result[-1]}')


if __name__ == '__main__':
    bot.infinity_polling()
