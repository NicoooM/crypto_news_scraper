import requests
import json
import csv
from datetime import datetime
import os

def generate_data(news_text):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ.get("API_KEY")
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Tu es un assistant virtuel qui aide les gens à comprendre les cryptomonnaies. En te donnant des informations sur l'actualité des cryptomonnaies, tu fais des résumés utilisant les informations les plus importantes. Tu rédiges ta réponse sous forme de liste à puces."},
            {"role": "user", "content": news_text}
        ],
        "temperature": 0.3,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()

    generated_text = response_json['choices'][0]['message']['content'].strip()

    file_exists = os.path.isfile('crypto_news.csv')

    with open('crypto_news.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Date", "Informations"])
        writer.writerow([datetime.now(), generated_text])