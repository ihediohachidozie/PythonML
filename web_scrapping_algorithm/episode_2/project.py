import requests 
from bs4 import BeautifulSoup
import re

site_map = "https://www.pngmart.com/sitemap.xml"
response = requests.get(site_map)
xml = response.text
soup = BeautifulSoup(xml, 'xml')

site_maps = []
for loc in soup.find_all('loc'):
  url = loc.text
  if 'posts' in url:
    #print(loc.text)
    site_maps.append(url)

# test demo
response = requests.get(site_maps[0])
soup = BeautifulSoup(response.text, 'xml')
#
master_list = []
for loc in soup.find_all('loc'):
  url = loc.text
  master_list.append(url)

counter = 0

for image_url in master_list[:10]:
  print(image_url)



  #break


#x = re.search(r"^https.*png$", png_url)


  
