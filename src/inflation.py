import requests
import secrets_stock_news

def get_inflation_rate():
    country = 'United States'
    api_url = 'https://api.api-ninjas.com/v1/inflation?country={}'.format(country)
    response = requests.get(api_url, headers={'X-Api-Key': secrets_stock_news.NINJA_API_KEY})
    if response.status_code == requests.codes.ok:
        print(response.json()[0]['period'], response.json()[0]['yearly_rate_pct'])
        # p = PostgresSQLPython()
        
    else:
        print("Error:", response.status_code, response.text)