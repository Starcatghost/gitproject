import telebot
import base_bot

bot = telebot.TeleBot(base_bot.TOKEN)
print('bot created ......')

video_url = "https://cdn1.movieland.af/movies/2025/yk-tsadf-sadh/yk-tsadf-sadh-720p-movieland.af.mp4"
photo_url = "https://www.technolife.com/image/gallery-3-TLP-167809_b1d8329d-e554-47a5-a5f3-dc4e8cc35b7c.png"
audio_url = "https://samplelib.com/lib/preview/mp3/sample-3s.mp3"
document_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"


@bot.message_handler(commands=['media'])
def show_media(message):
    markup = telebot.types.InlineKeyboardMarkup()

    btn1 = telebot.types.InlineKeyboardButton(text='local pic', callback_data='local_photo')
    btn2 = telebot.types.InlineKeyboardButton(text='online pic', callback_data='online_photo')
    markup.add(btn1 , btn2)

    btn3 = telebot.types.InlineKeyboardButton(text='local vid', callback_data='local_video')
    btn4 = telebot.types.InlineKeyboardButton(text='online vid', callback_data='online_video')
    markup.add(btn3 , btn4)

    btn5 = telebot.types.InlineKeyboardButton(text='local song', callback_data='local_audio')
    btn6 = telebot.types.InlineKeyboardButton(text='online song', callback_data='online_audio')
    markup.add(btn5 , btn6)


    btn7= telebot.types.InlineKeyboardButton(text='local doc', callback_data='local_doc')
    btn8 = telebot.types.InlineKeyboardButton(text='online doc ', callback_data='online_doc')
    markup.add(btn7 , btn8)

    bot.send_message(message.chat.id,text='chooose one of below options', reply_markup=markup)

    @bot.callback_query_handler(func=lambda call:True)
    def callback(call):
        call_id = call.message.chat.id


        if call.data == 'online_photo':
            bot.send_photo(call_id, photo_url, caption='show yourself i know you are watching me show yourself' )
        elif call.data == 'local_photo':
            with open('./media/images.jpg', 'rb') as photo:
                bot.send_photo(call_id,photo, caption="badass in the arina")
        
        elif call.data == 'online_video':
            bot.send_video(call_id, video_url, caption='show yourself i know you are watching me show yourself' )
        elif call.data == 'local_video':
            with open('./media/ice cream vid.mp4', 'rb') as video:
                bot.send_video(call_id,video, caption="badass in the arina")

        
        elif call.data == 'online_audio':
            bot.send_audio(call_id, audio_url, caption='show yourself i know you are watching me show yourself' )
        elif call.data == 'local_audio':
            with open('./media/Pony.mp3', 'rb') as audio:
                bot.send_audio(call_id,audio, caption="badass in the arina")

        
        elif call.data == 'online_doc':
            bot.send_document(call_id, document_url, caption='show yourself i know you are watching me show yourself' )
        elif call.data == 'local_doc':
            with open('./media/Artifical Inteligence-پاورپوینت هوش مصنوعی راسل.ppt', 'rb') as doc:
                bot.send_document(call_id,doc, caption="badass in the arina")


if __name__=='__main__':
    bot.infinity_polling()