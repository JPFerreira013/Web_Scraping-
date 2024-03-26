#Part 5: Top items being scraped right now

import requests

from bs4 import BeautifulSoup

#Make a request

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list

top_items = []

# Extract and store in top_items according to instructions on the left

productos = soup.select('div.thumbnail')

for elements in productos:
    title = elements.select('h4 > a.title')[0].text
    reviews = elements.select('div.ratings')[0].text
    
    info = {
    "title": title.strip(),
    "reviews": reviews.strip()
    }

#Append this dictionary in a list called top_items

top_items.append(info)

print(top_items)