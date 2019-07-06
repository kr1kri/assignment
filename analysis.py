import json
import os
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy


with open('file.json') as f:
    data = json.load(f)

comments = []

for item in data:
    comments.append(item["text"])

texts = '\n'.join(comments)

with open('gr_stopwords.txt') as f:
    mystopwords = f.read().splitlines()

wordcloud = WordCloud(max_font_size=40, relative_scaling=0.5, stopwords=mystopwords,
                      background_color="white").generate(texts)

plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcloud.png")

