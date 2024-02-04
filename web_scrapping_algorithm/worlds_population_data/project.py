import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


table = soup.find('table')

titles = [title.text.strip() for title in table.find_all('tr')[0]]

df_titles = [title for title in titles if title != ""]

df = pd.DataFrame(columns=df_titles)

column_data = table.find_all('tr')

data_list = []

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]
  individual_row_data.pop()
  data_list.append(individual_row_data)

df = pd.DataFrame(data_list, columns=df_titles)

df.to_csv('data\wiki_data.csv', index=False)
