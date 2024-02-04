import requests, csv, pandas as pd
from bs4 import BeautifulSoup

def main():
  with open('data/crypto_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(get_title())

  for x in range(1,90):
    for row in crypto_info(x):
      with open('data/crypto_data.csv', 'a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(row)


def get_title() -> list:
  url = "https://coinmarketcap.com/"
  page = requests.get(url)

  soup = BeautifulSoup(page.text, "html.parser")

  table = soup.find('table')

  titles = [title.text.strip() for title in table.find_all('th')]

  return titles

def crypto_info(num : int) -> list:

  data_list = []

  page = requests.get(f"https://coinmarketcap.com/?page={num}")

  soup = BeautifulSoup(page.text, "html.parser")

  table = soup.find('table')

  column_data = table.find_all('tr')

  for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [ data.text.strip() for data in row_data]
    data_list.append(individual_row_data)
  
  return data_list

if __name__ == "__main__":
  main()


 