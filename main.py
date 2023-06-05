from utils.news_scraper import scrape_latest_news
from utils.data_generator import generate_data
from dotenv import load_dotenv

load_dotenv()

websites = [
    "https://cryptoast.fr/",
    "https://www.cointribune.com/",
]

latest_news = []
for website in websites:
    scraped_news = scrape_latest_news(website)
    latest_news.extend(scraped_news)

news_text = " ".join(latest_news)

generate_data(news_text)