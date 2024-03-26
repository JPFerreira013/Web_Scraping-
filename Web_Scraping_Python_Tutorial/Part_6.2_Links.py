#Part 6.1: Extracting Links

import requests

from bs4 import BeautifulSoup

#Make a request

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content, 'html.parser')

# Create all_links as empty list
all_links = []

# Extract and store in top_items according to instructions on the left
links = soup.select('a')

for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''

    info = {
    'href': href,
    'text': text
    }
    all_links.append(info)
print(all_links)

'''for ahref in links:
    text = ahref.text.strip() if ahref.text else ''
    href = ahref.get('href').strip() if ahref.get('href') else ''

    info = {'href': href, 'text': text}
    all_links.append(info)
print(all_links)'''