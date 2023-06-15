import finnhub
import secrets_stock_news
import datetime


class Finnhub:

    def __init__(self) -> None:
        self.finnhub_client = finnhub.Client(api_key=secrets_stock_news.API_KEY)
        file_open = open('min_id.txt', 'r')
        self.min_id = int(file_open.readline())
        file_open.close()

    def read_news(self, topic='general'):
        
        news = self.finnhub_client.general_news(topic, self.min_id)

        self._update_min_id(news)
        
        return news

    def _update_min_id(self, news):
        id = []

        for n in news:
            id.append(n['id'])

        if(len(id)):
            self.min_id = max(id)
            file_open = open('min_id.txt', 'w')
            file_open.write(str(self.min_id))
            file_open.close()
            
    