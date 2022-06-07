import requests
from bs4 import BeautifulSoup


def get_first_news():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    url = 'https://gamebomb.ru/news'
    response = requests.get(url=url, headers=headers)
    suop = BeautifulSoup(response.text, 'html.parser')
    articles_cards = suop.find_all('div', class_='container-normal container-content')

    for article in articles_cards:
        articles = article.find_all('tr', class_='gbnews-listShort')
        for item in articles:
            article_title = item.find('p').get_text(strip=True)
            article_url = url + item.find('a').get('href')
            article_data_time = item.find('div', class_='sub').get_text(strip=True)


def main():
    get_first_news()


if __name__ == '__main__':
    main()