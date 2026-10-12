from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#  print(soup)

# latest_news = soup.find('div', attrs={'class':'medium-widget blog-widget'})
# print('len latest news: ', len(latest_news))
# print(latest_news)

# titles = latest_news.find_all('a')
# times = latest_news.find_all('time')
# print(title)


# for item in titles:
#     print(item.get_text())
#     print(item.get('href'))
#     print('*'*30)



# for item in times:
#     print(item.get_text())
#     print('-'*30)



############################


titles = soup.select('div.moudle-widget.event-widget.lastul.menu li a')
# print(titles)

for item in titles:
    print(item.get_text())