INSERT_QUERY_DEV = "INSERT INTO news_dev (category, datetime, headline, id, image, related, source, summary, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_QUERY_PROD = "INSERT INTO news (category, datetime, headline, id, image, related, source, summary, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

NEWS_LAST_7_DAYS_QUERY_DEV = '''
    SELECT *
    FROM news_dev
    WHERE CAST(TO_TIMESTAMP(datetime) AS date) > CURRENT_DATE - 7'''
NEWS_LAST_7_DAYS_QUERY_PROD = '''
    SELECT *
    FROM news
    WHERE CAST(TO_TIMESTAMP(datetime) AS date) > CURRENT_DATE - 7'''

NEWS_LAST_2_DAYS_QUERY_DEV = '''
    SELECT *
    FROM news_dev
    WHERE CAST(TO_TIMESTAMP(datetime) AS date) > CURRENT_DATE - 2'''
NEWS_LAST_2_DAYS_QUERY_PROD = '''
    SELECT *
    FROM news
    WHERE CAST(TO_TIMESTAMP(datetime) AS date) > CURRENT_DATE - 2'''
