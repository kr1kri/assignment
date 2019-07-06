import json
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy


with open('file.json') as f:
    data = json.load(f)

comments = []

for item in data:
    comments.append(item["text"])


wordcloud = WordCloud(max_font_size=40, relative_scaling=0.5, background_color="white").generate(" ".join(comments))

plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcloud.png")

