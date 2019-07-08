## Description

The purpose of this task was to design a procedure to extract the content from two threads of the https://www.insomnia.gr/ forum and export the harvested data and perform any kind of natural language processing or statistical analysis on the acquired dataset.

## Used Tools/Technologies

>Python 3.6  
>requests  
>pandas  
>WordCloud 
>matplotlib

## Implementation

### Part-1.

The first thing I decided to do, was to search and find a way to collect the data I needed from the two threads of the https://www.insomnia.gr/ forum. After some research on the web and specifically on GitHub, I chose to use the two Python libraries: 'requests' and 'BeautifulSoup'.
At first, I scrapped the urls with the ‘requests’ library, and then I extracted the data of the given URLs with the use of 'BeautifulSoup'.
Since I was asked to create a dataset with the messages, the usernames and the timestamps of the threads, I used the Mozilla Firefox Inspector tool to find the exact point of the HTML file I should select to find what was required. What I found was that the data I was looking for were inside an 'article' class. More specifically, the attributes I searched for comments were {"data-role" : "commentContent"}, for usernames were {"class": "ipsType_break"} and for timestamps was {'datetime'}.
Using a loop from the first to the last page of every thread, I stored all those values to a Python Dictionary with the labels ‘text’, ‘username’ and ‘timestamp’. And finally I extracted this dictionary to a JSON file so I could easier manipulate my dataset.
The above procedure is on the scrapper.py file.

## Author

Christou Christos christos.r.christou@gmail.com
