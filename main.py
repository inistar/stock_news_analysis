from finnhub_news_extractor import Finnhub
from psql_python import PostgresSQLPython
# from kafka_producer import Kafka

import sql_statements
import time

topic = 'stock_news'
TABLE_NAME = None

if(sql_statements.ENV == 'DEV'):
    # INSERT_QUERY = sql_statements.INSERT_QUERY_DEV
    TABLE_NAME = sql_statements.TABLE_NAME_DEV
else:
    # INSERT_QUERY = sql_statements.INSERT_QUERY_PROD
    TABLE_NAME = sql_statements.TABLE_NAME_PROD

if __name__ == '__main__':
    print("Starting stock analysis pipeline....")
    # k = Kafka()
    f = Finnhub()
    p = PostgresSQLPython()

    while(True):
        news = f.read_news()

        print(f'Read: {len(news)}')
        # for n_dict in news:
            # k.send('stock_news', str(i).encode('utf-8'), str(i).encode('utf-8'))
            # k.send(topic, value=n_dict)

        if(len(news)):
            news = f.find_sentiment(news)
            p.batch_insert(news, TABLE_NAME)
    
            f.update_min_id(news)

        time.sleep(1000)

    # k.flush()
    # k.close()
    p.close()


