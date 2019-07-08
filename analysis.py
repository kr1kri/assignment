#import modules
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

#read the dataset
with open('file.json', 'r') as f:
    data = json.load(f)

#categories to execute wordcloud
categories = ["text", "username"]

#add stopwords for wordcloud
mystopwords = []

#pass the text of gr_stopwords as stopwords for wordcloud
with open('gr_stopwords.txt') as f:
    mystopwords = f.read().splitlines()

#wordclouds creation
for x in range (len(categories)):
    column = []

    for item in data:
        column.append(item[categories[x]])

    text = '\n'.join(column)

    wordcloud = WordCloud(width=1600, height=800, stopwords=mystopwords, background_color="white").generate(text)

    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("wordcloud_" + categories[x] + ".png")

#initialize a dataframe with the publish timespamp
df = pd.DataFrame([[pd.to_datetime(x['timestamp']),i] for i,x in enumerate(data)], columns=['timespamp', 'id'])

#group by year and month in order to visualize the distribution of the publish date
ax = df.groupby([df["timespamp"].dt.year, df["timespamp"].dt.month, df["timespamp"].dt.day])['id'].count().plot(title='Publish Date Distribution')
ax.set_ylabel("number of posts")
ax.set_xlabel("date")

plt.savefig("publish_date.png")

#group by hour in order to visualize the distribution of the publish time
ax = df.groupby([df["timespamp"].dt.hour])['id'].count().plot(title='Publish Time Distribution')
ax.set_ylabel("number of posts")
ax.set_xlabel("hour of day")

plt.savefig("publish_time.png")



