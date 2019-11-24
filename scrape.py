from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

page_link = 'https://webapps1.chicago.gov/landmarksweb/web/listings.htm'

page_response = requests.get(page_link,timeout=5)

soup= BeautifulSoup(page_response.content, "html.parser")

info = soup.find('table', attrs={'class', 'homeTB2'})
name = info.text.strip()
print(name)

with open('index.csv', 'a') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow([name, datetime.now()])
