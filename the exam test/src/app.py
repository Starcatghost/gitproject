import telebot
import sqlite3
import base_bot
import app1

bot = telebot.TeleBot(base_bot.TOKEN)

DB_NAME = 'MobileProduct.db'


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        'Welcome to our TechnoLife bot!\n'
        '/update - Update products\n'
        '/products - Show products\n'
        '/search - Search products\n'
        '/cheapest - Cheapest product\n'
        '/history - Price history'
    )

@bot.message_handler(commands=['update'])
def update(message):
    try:
        app1.update_products()
        bot.reply_to(message, 'Products updated ;)')
    except Exception:
        bot.reply_to(message, 'Error updating products')


@bot.message_handler(commands=['products'])
def products(message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT title, price, link FROM MobileData')
    rows = cursor.fetchall()

    if not rows:
        bot.reply_to(message, 'No products were found')
    else:
        for row in rows:
            bot.send_message(
                message.chat.id,
                f'Name: {row[0]}\n'
                f'Price: {row[1]}\n'
                f'Link: {row[2]}'
            )

    conn.close()


@bot.message_handler(commands=['search'])
def search(message):
    name = message.text.replace('/search', '').strip()

    if not name:
        bot.reply_to(message, 'Example: /search سامسونگ (write it in farsi)')
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT title, price, link FROM MobileData WHERE title LIKE ?',
        ('%' + name + '%',)
    )

    rows = cursor.fetchall()

    if not rows:
        bot.reply_to(message, 'Product not found.')
    else:
        for row in rows:
            bot.send_message(
                message.chat.id,
                f'Name: {row[0]}\n'
                f'Price: {row[1]}\n'
                f'Link: {row[2]}'
            )

    conn.close()


@bot.message_handler(commands=['cheapest'])
def cheapest(message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT title, price, link
        FROM MobileData
        WHERE price IS NOT NULL AND price != ''
        ORDER BY CAST(REPLACE(price, ',', '') AS INTEGER)
        LIMIT 1
        '''
    )

    row = cursor.fetchone()

    if row:
        bot.reply_to(
            message,
            f'Name: {row[0]}\n'
            f'Price: {row[1]}\n'
            f'Link: {row[2]}'
        )
    else:
        bot.reply_to(message, 'No products were found :(')

    conn.close()


@bot.message_handler(commands=['history'])
def history(message):
    bot.reply_to(message, 'Price history is not available yet')


bot.infinity_polling()
