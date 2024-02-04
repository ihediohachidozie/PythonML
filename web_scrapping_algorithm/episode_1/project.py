import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

def main():
  if len(sys.argv) < 3:
    sys.exit("Incomplete command")
  elif len(sys.argv) == 3:
    try:
      first = abs(int(sys.argv[1]))
      last = abs(int(sys.argv[2]))
      print(process_data_2(first, last))
    except ValueError:
      sys.exit("Invalid entry")


def get_clinic_name(clinic_id) -> str:
  url = f"https://{clinic_id}.portal.athenahealth.com/"
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  clinic_name = soup.find_all('h1')[-1].text.strip()
  if clinic_name not in ["Sorry, we can't find that practice. Make sure you typed the right address.", "Payment Confirmation"]:
    return clinic_name


def process_data(n, m) -> str:
  clinic_list = []

  for clinic_id in range(n, m + 1):
    name = get_clinic_name(clinic_id)
    if name != None:
      data_dict = {}
      data_dict['clinic_id'] = clinic_id
      data_dict['clinic_name'] = name
      clinic_list.append(data_dict)
  df = pd.DataFrame(clinic_list)
  df.to_csv('clinic_data.csv', index=False)
  return "Task Completed successfully!"


def process_data_2(n, m) -> str:
  df = pd.DataFrame(columns=["Id", "Clinic Names"])
  for id in range(n, m + 1):
    if name := get_clinic_name(id):
      length = len(df)
      df.loc[length] = [id, name]
  
  df.to_csv("clinic_data.csv", index=False)
  return "Task Completed successfully!"
      
  



if __name__ == "__main__":
  main()