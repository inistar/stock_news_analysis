import finnhub
import secrets_stock_news
import requests
import sql_statements
import pandas as pd
import time

MIN_ID_FILE = None

if(sql_statements.ENV == 'DEV'):
    MIN_ID_FILE = sql_statements.MIN_ID_DEV
else:
    MIN_ID_FILE = sql_statements.MIN_ID_PROD

class Finnhub:

    def __init__(self) -> None:
        self.finnhub_client = finnhub.Client(api_key=secrets_stock_news.API_KEY)
        file_open = open(MIN_ID_FILE, 'r')
        self.min_id = int(file_open.readline())
        file_open.close()

    def read_news(self, topic='general'):
        
        news = self.finnhub_client.general_news(topic, self.min_id)

        # self._update_min_id(news)
        
        return news

    def _query(self, payload, headers):
        response = requests.post(secrets_stock_news.HF_API_URL, headers=headers, json=payload)
        return response.json()

    def find_sentiment(self, df):
        headers = {"Authorization": f"Bearer {secrets_stock_news.HF_API_TOKEN}"}

        df = pd.DataFrame(df)
        
        inputs = df['summary'].to_list()
        payload = {"inputs": inputs}

        outputs = None
        count = 0
        while(not outputs):
            outputs = self._query(payload, headers)
            if(count > 2):
                break
            count += 1
            print("Sleeping...")
            time.sleep(5)


        sentiment = []
        # print(outputs)
        for output in outputs:
            sentiment.append(output[0]['label'])

        df['sentiment'] = sentiment

        return df


    def update_min_id(self, news):
        self.min_id = news['id'].max()
        file_open = open(MIN_ID_FILE, 'w')
        file_open.write(str(self.min_id))
        file_open.close()
            
    