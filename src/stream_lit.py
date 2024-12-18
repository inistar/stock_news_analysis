import streamlit as st
import pandas as pd
from stock_news_analysis.src.psql_python import PostgresSQLPython
import stock_news_analysis.src.sql_statements as sql_statements
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords

NEWS_LAST_2_DAYS_QUERY = None
NEWS_LAST_7_DAYS_QUERY = None

if(sql_statements.ENV == 'DEV'):
    NEWS_LAST_2_DAYS_QUERY = sql_statements.NEWS_LAST_2_DAYS_QUERY_DEV
    NEWS_LAST_7_DAYS_QUERY = sql_statements.NEWS_LAST_7_DAYS_QUERY_DEV
else:
    NEWS_LAST_2_DAYS_QUERY = sql_statements.NEWS_LAST_2_DAYS_QUERY_PROD
    NEWS_LAST_7_DAYS_QUERY = sql_statements.NEWS_LAST_7_DAYS_QUERY_PROD


st.title('News Analysis')

NEWS_7_DAYS = None
NEWS_2_DAYS = None

p = PostgresSQLPython()

@st.cache_data
def load_2_days_data():
    return p.read_query(NEWS_LAST_2_DAYS_QUERY)

def load_7_days_data():
    return p.read_query(NEWS_LAST_7_DAYS_QUERY)

data_load_state = st.text('Loading data...')
NEWS_2_DAYS = load_2_days_data()
NEWS_7_DAYS = load_7_days_data()
data_load_state.text("Done! (using st.cache_data)")

st.subheader('Raw data of Last 2 Days')
st.write(NEWS_2_DAYS[[9,6,7,8]])

def generate_wordcloud(text):
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()

    filler_words = set(stopwords.words('english'))
    filler_words.update(['said',
                         'say',
                         'stock',
                         'year',
                         'may',
                         'monday',
                         'tuesday',
                         'wednesday',
                         'thursday',
                         'friday',
                         'saturday',
                         'sunday',
                         'us',
                         'company',
                         'week',
                         'stock',
                         'share',
                         'shares',
                         'day',
                         'june',
                         'investor',
                         'investors',
                         'year-to-date',
                         'years',
                         'month',
                         'days',
                         'according',
                         'another',
                         'analyst',
                         'market',
                         "new",
                         "stocks",
                         "top",
                         "million",
                         "see",
                         "first",
                         "economy",
                         "last",
                         "inc",
                         "companies"
                         ])

    filtered_tokens = [word.lower() for word in tokens if word.lower() not in filler_words]

    # Create WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(' '.join(filtered_tokens))

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt.gcf())

st.subheader('Word Cloud Last 2 Days')
combined_str = NEWS_2_DAYS[7].str.cat(sep=' ')
generate_wordcloud(combined_str)

st.subheader('Word Cloud Last 7 Days')
combined_str = NEWS_7_DAYS[7].str.cat(sep=' ')
generate_wordcloud(combined_str)


# st.subheader('Number of pickups by hour')

# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

# st.bar_chart(hist_values)

# hour_to_filter = 17
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# st.map(filtered_data)

# hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h



