import requests
from bs4 import BeautifulSoup

def scrape_latest_news(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news = [] 
        news_headlines = soup.find_all('h2')
        news_preview = soup.find_all('h3')

        for headline in news_headlines:
            news.append(headline.text.strip())
        for preview in news_preview:
            news.append(preview.text.strip())
        return news
    else:
        print(f"Failed to scrape news from {url}")
        return []