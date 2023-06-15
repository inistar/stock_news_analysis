from finnhub_news_extractor import Finnhub
from kafka_producer import Kafka
import time

topic = 'stock_news'

if __name__ == '__main__':
    print("Starting stock analysis pipeline....")
    k = Kafka()
    f = Finnhub()

    while(True):
        news = f.read_news()

        print(f'Read: {len(news)}')
        for n_dict in news:
            # k.send('stock_news', str(i).encode('utf-8'), str(i).encode('utf-8'))
            k.send(topic, value=n_dict)
    
        time.sleep(60)

    k.flush()
    k.close()


