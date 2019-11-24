import geocoder
import csv
import pandas as pd

my_csv = pd.read_csv('add.csv')
geo_csv = csv.writer(open('geo.csv','w'))

for add in my_csv['address']:
    g = geocoder.google(add)
    g_latlng = g.latlng
    geo_csv.writerow([g_latlng])
