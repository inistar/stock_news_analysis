from finnhub_news_extractor import Finnhub
from kafka_producer import Kafka



if __name__ == '__main__':
    print("Starting stock analysis pipeline....")

    f = Finnhub()
    news = f.read_news()
    print(news)

    # k = Kafka()
    # for i in range(100):
    #     k.send('stock_news', str(i).encode('utf-8'), str(i).encode('utf-8'))
    
    # k.flush()


