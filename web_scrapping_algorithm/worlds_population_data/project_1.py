import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/world-population/population-by-country/"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

table = soup.find('table')

titles = [title.text.strip() for title in table.find_all('th')]


df = pd.DataFrame(columns=titles)

column_data = table.find_all('tr')

data_list = []

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]

  length = len(df)
  df.loc[length] = individual_row_data

df.to_csv('data\worldometer_data.csv', index=False)
 
