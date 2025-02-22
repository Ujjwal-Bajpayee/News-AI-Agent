import requests
from bs4 import BeautifulSoup

def fetch_news_articles(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for item in soup.find_all('a', class_='gs-c-promo-heading'):
        title = item.text.strip()
        link = "https://www.bbc.com" + item['href']
        articles.append({'title': title, 'link': link})
    
    return articles