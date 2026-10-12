import requests
import sqlite3
from bs4 import BeautifulSoup


url = 'https://www.technolife.com/category/mobile/mobile-phone'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


DB_NAME = 'MobileProduct.db'
conn = sqlite3.connect(DB_NAME)

query = '''CREATE TABLE IF NOT EXISTS MobileData
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
price TEXT,
image TEXT,
link TEXT,
description TEXT,
brand TEXT,
storage TEXT,
ram TEXT,
color TEXT,
rating TEXT
)
'''

cursor = conn.cursor()
cursor.execute(query)
conn.commit()

print('table created')


cards = soup.select('section.relative.w-full.rounded-\\[10px\\]')


for card in cards:

    title = card.find('h2')

    if title is None:
        continue

    title = title.text.strip()
    print(title)


    price = card.select_one(
        'p.text-\\[22px\\].font-semiBold.leading-5'
    )

    if price is None:
        continue

    price = price.text.strip()
    print(price)


    image = card.select_one('a[href^="/product-"] img')

    if image is None:
        continue

    image = image.get('src')
    img_url = 'https://www.technolife.com' + image


    link = 'https://www.technolife.com' + card.select_one(
        'a[href^="/product-"]'
    ).get('href')


    response2 = requests.get(link)
    soup2 = BeautifulSoup(response2.text, 'html.parser')


    description = soup2.find(
        'meta',
        {'name': 'description'}
    )

    if description is None:
        description = ''
    else:
        description = description.get('content')



    brand = soup2.find(string='Brand')

    if brand is None:
        brand = ''
    else:
        brand = brand.parent.parent.text.strip()




    storage = soup2.find(string='Internal storage')

    if storage is None:
        storage = ''
    else:
        storage = storage.parent.parent.text.strip()



    ram = soup2.find(string='RAM')

    if ram is None:
        ram = ''
    else:
        ram = ram.parent.parent.text.strip()



    color = soup2.find(string='Color')

    if color is None:
        color = ''
    else:
        color = color.parent.parent.text.strip()



    rating = soup2.find(string='User rating')

    if rating is None:
        rating = ''
    else:
        rating = rating.parent.parent.text.strip()


    query = '''
        INSERT INTO MobileData
        (title, price, image, link, description,
         brand, storage, ram, color, rating)
        VALUES(?,?,?,?,?,?,?,?,?,?)
    '''


    cursor.execute(query,(title,price,img_url,link,description,brand,storage,ram,color,rating))
    conn.commit()


conn.close()

print('WEB DATA Scraped')