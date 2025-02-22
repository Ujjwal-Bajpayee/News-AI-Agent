from modules.crawler import fetch_news_articles
from modules.summarizer import summarize_text
from modules.seo_optimizer import extract_keywords
from modules.publisher import publish_to_wordpress
import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.bbc.com/news"
    articles = fetch_news_articles(url)
    for article in articles:
        print(f"Processing article: {article['title']}")
        article_response = requests.get(article['link'])
        if article_response.status_code != 200:
            print(f"Failed to fetch article: {article['link']}")
            continue
        article_soup = BeautifulSoup(article_response.text, 'html.parser')
        article_text = " ".join([p.text for p in article_soup.find_all('p')])
        summary = summarize_text(article_text)
        print(f"Summary: {summary}")
        keywords = extract_keywords(article_text)
        print(f"Keywords: {keywords}")
        try:
            publish_to_wordpress(article['title'], summary)
            print(f"Published: {article['title']}")
        except Exception as e:
            print(f"Failed to publish article: {e}")
if __name__ == "__main__":
    main()