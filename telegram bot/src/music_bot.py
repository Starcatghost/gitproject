import telebot
import base_bot
from api_hw_music import get_music

bot = telebot.TeleBot(base_bot.TOKEN)
print('bot created ...')

@bot.message_handler(commands=['music'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Enter music name:')
    bot.register_next_step_handler(msg, search_music)


def search_music(message):
    result = get_music(message.text)

    if result == 'ERROR':
        bot.send_message(message.chat.id, 'API ERROR')
    elif result:
        name, url = result
        bot.send_message(message.chat.id, f'name of the movie: {name} and the URL: {url}')
    else:
        bot.send_message(message.chat.id, 'Music not found')


bot.infinity_polling()
