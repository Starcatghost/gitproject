import requests
import sqlite3

from bs4  import BeautifulSoup  



url= 'https://www.technolife.com/category/mobile/mobile-phone'
response = requests.get(url)
soup = BeautifulSoup (response.text, 'html.parser')

DB_NAME = 'MobileProduct.db'
conn = sqlite3.connect(DB_NAME)

query = '''CREATE TABLE IF NOT EXISTS MobileData
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
price TEXT,
image TEXT,
link TEXT
)
'''
cursor = conn.cursor()
cursor.execute(query)
conn.commit()
# conn.close()
print ('table created')

cards = soup.select('section.relative.w-full.rounded-\\[10px\\]')


for card in cards:

    title = card.find('h2').text.strip()
    if title == None :
        continue

    print(title)

    price = card.select_one('p.text-\\[22px\\].font-semiBold.leading-5').text.strip()
    if price == None:
        continue

    print(price)

    image = card.select_one('a[href^="/product-"] img').get('src')
    img_url = 'https://www.technolife.com'+ image

    #print(img_url)

    link = 'https://www.technolife.com' + card.select_one('a[href^="/product-"]').get('href')
    
    query = '''
            INSERT INTO MobileData(title, price, image, link)
            VALUES(?,?,?,?) 
            '''
    cursor.execute(query, (title, price, image, link))
    conn.commit()



conn.close()
print('WEB DATA Scraped')