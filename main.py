import requests
from bs4 import BeautifulSoup
import json


def get_first_news():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    url = 'https://gamebomb.ru/news'
    response = requests.get(url=url, headers=headers)
    suop = BeautifulSoup(response.text, 'html.parser')
    articles_cards = suop.find_all('div', class_='container-normal container-content')

    news_dict = {}

    for article in articles_cards:
        articles = article.find_all('tr', class_='gbnews-listShort')
        for item in articles:
            article_title = item.find('p').get_text(strip=True)
            article_url = url + item.find('a').get('href')
            article_data_time = item.find('div', class_='sub').get_text(strip=True)

            article_id = article_url.split('/')[-1]  # get news id

            news_dict[article_id] = {
                'article_title': article_title,
                'article_url': article_url,
                'article_data_time': article_data_time
            }

        with open('news_dict.json', 'w', encoding='utf-8') as file:
            json.dump(news_dict, file, indent=4, ensure_ascii=False)


def check_news():
    with open('news_dict.json', encoding='utf-8') as file:
        news_dict = json.load(file)

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    url = 'https://gamebomb.ru/news'
    response = requests.get(url=url, headers=headers)
    suop = BeautifulSoup(response.text, 'html.parser')
    articles_cards = suop.find_all('div', class_='container-normal container-content')

    latest_news = {}

    for item in articles_cards:
        article_url = url + item.find('a').get('href')
        article_id = article_url.split('/')[-1]

        if article_id in news_dict:
            continue
        else:
            article_title = item.find('p').get_text(strip=True)
            article_data_time = item.find('div', class_='sub').get_text(strip=True)

            news_dict[article_id] = {
                'article_title': article_title,
                'article_url': article_url,
                'article_data_time': article_data_time
            }   # add new news

            latest_news[article_id] ={
                'article_title': article_title,
                'article_url': article_url,
                'article_data_time': article_data_time
            }   # dictionary for breaking news

    with open('news_dict.json', 'w', encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return latest_news


def main():
    get_first_news()


if __name__ == '__main__':
    main()