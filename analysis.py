import json
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy

#read the dataset
with open('file.json') as f:
    data = json.load(f)

categories = ["text", "username"]

#create stopwords for wordcloud
mystopwords = []

#pass the text of gr_stopwords as stopwords for wordcloud
with open('gr_stopwords.txt') as f:
    mystopwords = f.read().splitlines()

#create wordclouds
for x in range(len(categories)):
    column = []

    for item in data:
        column.append(item[categories[x]])

    text = '\n'.join(column)

    wordcloud = WordCloud(width=1600, height=800, stopwords=mystopwords, background_color="white").generate(text)

    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("wordcloud" + categories[x] + ".png")


