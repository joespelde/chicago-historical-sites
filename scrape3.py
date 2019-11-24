from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import time
import re

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

my_csv = pd.read_csv('sites.csv')
urls = my_csv.link
url= []
name_csv = csv.writer(open('name.csv','w'))
desc_csv = csv.writer(open('desc.csv','w'))
address_csv = csv.writer(open('address.csv','w'))
desc_csv.writerow(['des'])
name_csv.writerow(['nam'])
address_csv.writerow(['address'])
name = []
addresses = []
desc = []
for lin in my_csv['link']:
    url = lin
    content = requests.get(url)
    req = requests.get(url, headers)
    soup = BeautifulSoup(content.text, 'html.parser')
    name.append(soup.find_all("table",{"class":"insideTB1"}))
    desc.append(soup.find_all("span",{"class":"normal"}))
    # addresses.append(soup.findAll('td', sting = re.compile('Add')))
for nam in name:
    name_csv.writerow([nam])
for des in desc:
    desc_csv.writerow([des])
# for address in addresses:
#     address_csv.writerow([address])
# print(name)
# print(desc)
