#Part 2: Extracting title with BeautifulSoup
import requests

from bs4 import BeautifulSoup

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title.text

print(page_title)