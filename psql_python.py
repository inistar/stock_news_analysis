import psycopg2
import secrets_stock_news
import pandas as pd

class PostgresSQLPython():

    def __init__(self):
        self.conn = psycopg2.connect(
            host=secrets_stock_news.PSQL_HOST,
            database=secrets_stock_news.PSQL_DATABASE,
            user=secrets_stock_news.PSQL_USER,
            password=secrets_stock_news.PSQL_PASSWORD,
            port=secrets_stock_news.PSQL_PORT
        )

    def batch_insert(self, news, insert_query):
        with self.conn.cursor() as cursor:
            try:
                # Execute multiple INSERT statements in a single transaction
                cursor.executemany(insert_query, [tuple(item.values()) for item in news])

                # Commit the transaction
                self.conn.commit()

                print("Data inserted successfully!")
            except (Exception, psycopg2.DatabaseError) as error:
                # Rollback the transaction in case of an error
                self.conn.rollback()
                print("Error occurred during data insertion:", error)

    def read_query(self, query):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(query)
                rows = cursor.fetchall()
                return self.convert_to_df(rows)
            except (psycopg2.Error, Exception) as error:
                print("Error connecting to PostgreSQL:", error)

        return None
    
    def convert_to_df(self, data):
        return pd.DataFrame(data)
    
    def close(self):
        self.conn.close()