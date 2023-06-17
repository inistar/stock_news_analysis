from finnhub_news_extractor import Finnhub
from psql_python import PostgresSQLPython
# from kafka_producer import Kafka

import insert_sql_statements
import time

topic = 'stock_news'

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
            p.batch_insert(news, insert_sql_statements.INSERT_QUERY_DEV)
    
        time.sleep(1000)

    # k.flush()
    # k.close()
    p.close()


