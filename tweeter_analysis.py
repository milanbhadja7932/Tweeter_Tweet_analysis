# -*- coding: utf-8 -*-
"""tweeter_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NoymkGcy5mD86T9kFGwz7pZdBkGUUeEN
"""

import json
import numpy as np

#convert json into csv

import pandas as pd
df = pd.read_csv('/content/sample_data/tweets.csv')
df.head(10)



"""Preprocessing step"""



!pip install tweet-preprocessor

import preprocessor as p
train_df = pd.read_csv('/content/sample_data/tweets.csv')

train_df.count()

train_df = train_df.dropna()
train_df = train_df.drop_duplicates()

train_df.count()

train_df.head()



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from html.parser import HTMLParser
html_parser = HTMLParser()

train_df['clean_tweet'] = train_df['tweet_text'].apply(lambda x: html_parser.unescape(x))
train_df.head(10)

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt

train_df['clean_tweet'] = np.vectorize(remove_pattern)(train_df['clean_tweet'], "@[\w]*")
train_df.head(10)



train_df['clean_tweet'] = train_df['clean_tweet'].apply(lambda x: x.lower())
train_df.head(10)

train_df['clean_tweet'] = train_df['clean_tweet'].apply(lambda x: re.sub(r'[^\w\s]',' ',x))
train_df.head(10)

train_df['clean_tweet'] = train_df['clean_tweet'].apply(lambda x: re.sub(r'[^a-zA-Z0-9]',' ',x))
train_df.head(10)

train_df['clean_tweet'] = train_df['clean_tweet'].apply(lambda x: re.sub(r'[^a-zA-Z]',' ',x))
train_df.head(10)

train_df['clean_tweet'] = train_df['clean_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>1]))
train_df['clean_tweet'][0:5]

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

train_df['tweet_token'] = train_df['clean_tweet'].apply(lambda x: word_tokenize(x))

## Fully formated tweets & there tokens
train_df.head(10)

stop_words = set(stopwords.words('english'))
stop_words

train_df['tweet_token_filtered'] = train_df['tweet_token'].apply(lambda x: [word for word in x if not word in stop_words])

from nltk.stem import PorterStemmer
stemming = PorterStemmer()

train_df['tweet_stemmed'] = train_df['tweet_token_filtered'].apply(lambda x: ' '.join([stemming.stem(i) for i in x]))
train_df['tweet_stemmed'].head(10)

from nltk.stem.wordnet import WordNetLemmatizer
lemmatizing = WordNetLemmatizer()

nltk.download('wordnet')

train_df['tweet_lemmatized'] = train_df['tweet_token_filtered'].apply(lambda x: ' '.join([lemmatizing.lemmatize(i) for i in x]))
train_df['tweet_lemmatized'].head(10)



words_in_tweet = [tweet.lower().split() for tweet in train_df['tweet_lemmatized']]

import itertools
import collections
all_words_no_urls = list(itertools.chain(*words_in_tweet))

# Create counter
counts_no_urls = collections.Counter(all_words_no_urls)

counts_no_urls.most_common(50)

words_in_tweeter = [tweet.lower().split() for tweet in train_df['tweet_stemmed']]

import itertools
import collections
all_words_no_urls = list(itertools.chain(*words_in_tweeter))

# Create counter
counts_no_urls = collections.Counter(all_words_no_urls)

counts_no_urls.most_common(50)

import matplotlib.pyplot as plt
all_words = ' '.join([text for text in train_df['tweet_stemmed']])
from wordcloud import WordCloud
wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)

plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.title("Most Common words in column Tweet Stemmed")
plt.show()

tweet_counter = pd.DataFrame(counts_no_urls.most_common(25),
                             columns=['words', 'count'])
tweet_counter.head()

fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
tweet_counter.sort_values(by='count').plot.barh(x='words',
                      y='count',
                      ax=ax,
                      color="purple")

ax.set_title("Common Words Found in Tweets (Without Stop or Collection Words)")

plt.show()

from textblob import TextBlob

i=0
for tweet in train_df['tweet_lemmatized']:
  analysis = TextBlob((tweet))
        # set sentiment
  i=i+1
  if analysis.sentiment.polarity > 0:
    print("Author"+str(i),'positive')
  elif analysis.sentiment.polarity == 0:
    print("Author"+str(i),'positive', '    ','negative')
  else:
    print("Author"+str(i),'negative')

