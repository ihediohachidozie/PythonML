# Scrapping data from a Real Website + Pandas

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
#print(page.status_code)
# 1 - List of largest companies in the United States by revenue
# 2 - List of largest private companies
# 3 - List of companies by profit

table = soup.find_all('table')[3] # 


table_titles =[title.text.strip() for title in table.find_all('th')]
#print(table_titles)
df = pd.DataFrame(columns=table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]
  
  length = len(df)
  df.loc[length] = individual_row_data

df.to_csv('companies_by_revenue.csv', index=False)