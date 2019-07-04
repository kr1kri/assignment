#import modules
import requests
import json
from bs4 import BeautifulSoup

#list with the ulrs to scrap
my_urls = ["https://www.insomnia.gr/forums/topic/697881-amd-radeon-vii/", "https://www.insomnia.gr/forums/topic/706516-%CE%BA%CE%AC%CF%81%CF%84%CE%B5%CF%82-%CE%B3%CF%81%CE%B1%CF%86%CE%B9%CE%BA%CF%8E%CE%BD-amd-navi/"]

data = []

for item in my_urls:

#http request
    r = requests.get(       item)

#extract data from html
    soup = BeautifulSoup(r.content, 'html.parser')

    #find last page number for the loop
    last_url = soup.findAll('a', attrs={'rel': 'last'})
    if last_url:
      last_page = last_url[0].attrs['data-page']
      print (last_page)


    #loop from the first to last page of the thread
    for x in range(int(last_page)):

        articles = soup.findAll("article")

    #find the comment, username, and datetime and save them in data
        for article in articles:
            comment_elem = article.find(attrs={"data-role" : "commentContent"})
            text = '\n'.join(_.text for _ in comment_elem.findAll('p'))
            username = article.find(attrs={"class": "ipsType_break"}).text
            time = article.find('time').attrs['datetime']
            data.append({
               'text': text.strip(),
               'username': username.strip(),
               'timestamp': time.strip()
            })

    #get next page url
        next_url = soup.findAll('a', attrs={'rel': 'next'})
        if next_url:
            nextp_url = next_url[0].attrs['href']

    #http request on the next page of thread --- error here!
        r = requests.get(nextp_url)

    #extract data of the next page of thread
        soup = BeautifulSoup(r.content, 'html.parser')

#export data to a json file
with open('file.json', 'w' ) as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
