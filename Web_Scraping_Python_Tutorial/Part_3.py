#Part 3: Soup-ed body and head

import requests

from bs4 import BeautifulSoup

#Make a request

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title

# Extract head of page
page_head = soup.head

# Extract body of page
page_body = soup.body

# print the result
print(page_title, page_head, page_body)
