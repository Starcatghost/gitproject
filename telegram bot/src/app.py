import telebot
import base_bot
import app_api

bot = telebot.TeleBot(base_bot.TOKEN)

print('bot created ...')

@bot.message_handler(commands=['start'])
def send_message(message):
    #print(message)
    bot.send_message(message.chat.id, text = "welcome to my bot lovely")

@bot.message_handler(commands=['help' ,'signup'])
def reply_message(message):
    bot.reply_to(message, text= "in case of need help message @frrreakkk ")


@bot.message_handler(commands= ['list'])
def show_list(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn1 = telebot.types.InlineKeyboardButton(text= "about hyun", url= 'https://varzesh3.com')
    btn2 = telebot.types.InlineKeyboardButton(text= "about jay", url= 'https://entekhab.ir')
    markup.add(btn1 , btn2)
    bot.send_message(message.chat.id, text= "choose one of your lovers: ", reply_markup=markup)


@bot.message_handler(commands=['movie'])
def show_msg(message):
    msg = bot.send_message(message.chat.id, 'give me the name of the movie: ')
    bot.register_next_step_handler(msg, show_movie_info)

def show_movie_info(message):
    movie_name = message.text

    result = app_api.get_movie_info_by_name(movie_name)
    info = f'title: {result[0]} / year: {result[1]}'
    bot.send_message(message.chat.id, info)    


@bot.message_handler(commands=['menu']) 
def show_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    btn3 = telebot.types.KeyboardButton(text= 'I love Jay')
    btn4 = telebot.types.KeyboardButton(text= 'I love Hyun')
    btn5 = telebot.types.KeyboardButton(text= 'I love Aylin')
    markup.add(btn3,btn4,btn5)
    bot.send_message(message.chat.id, text= "who do you love: ", reply_markup=markup)

@bot.message_handler(func = lambda message: True)
def answer_to_other_message(message):
    if message.text == 'I love Jay':
        descrirption = "you like the rich big guy"
        bot.send_message(message.chat.id, text= descrirption)

    elif message.text == 'I love Hyun':
        email = "aylinh684@gmail.com"
        mobile = "09031658475"
        office_add = "@frrreakkk"
        info = f'email: {email} and mobile num {mobile} and also our teegram id {office_add}'
        bot.reply_to(message, text= info)

    elif message.text == 'I love Aylin':
        markup = telebot.types.ReplyKeyboardMarkup()    
        bot.send_message(message.chat.id, text= "back to the main menu ", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text= "fuck you biitch")




if __name__=='__main__':
    bot.infinity_polling()
