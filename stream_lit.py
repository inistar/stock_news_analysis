import streamlit as st
import pandas as pd
from psql_python import PostgresSQLPython
import sql_statements
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

st.title('News Analysis')

NEWS_7_DAYS = None
NEWS_2_DAYS = None

p = PostgresSQLPython()

@st.cache_data
def load_2_days_data():
    return p.read_query(sql_statements.NEWS_LAST_2_DAYS_QUERY_PROD)

def load_7_days_data():
    return p.read_query(sql_statements.NEWS_LAST_7_DAYS_QUERY_PROD)

data_load_state = st.text('Loading data...')
NEWS_2_DAYS = load_2_days_data()
NEWS_7_DAYS = load_7_days_data()
data_load_state.text("Done! (using st.cache_data)")

st.subheader('Raw data')
st.write(NEWS_2_DAYS)



st.subheader('Word Cloud Last 7 Days')
def generate_wordcloud(text):

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
                         'year'
                         ])

    filtered_tokens = [word.lower() for word in tokens if word.lower() not in filler_words]

    # Create WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(' '.join(filtered_tokens))

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt.gcf())

combined_str = NEWS_7_DAYS[7].str.cat(sep=' ')
generate_wordcloud(combined_str)



st.subheader('Word Cloud Last 2 Days')
# def generate_wordcloud(text):
#     # Create WordCloud object
#     wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

#     # Display the word cloud using matplotlib
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation="bilinear")
#     plt.axis("off")
#     st.pyplot(plt.gcf())

combined_str = NEWS_2_DAYS[7].str.cat(sep=' ')
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



