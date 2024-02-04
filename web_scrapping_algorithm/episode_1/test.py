import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys


def get_clinic_name(clinic_id) -> str:
  url = f"https://{clinic_id}.portal.athenahealth.com/"
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  clinic_name = soup.find_all('h1')

  return clinic_name
    
print(get_clinic_name(11000))