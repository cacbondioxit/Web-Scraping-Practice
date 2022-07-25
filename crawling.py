import pandas as pd
import numpy as np 
import requests
from bs4 import BeautifulSoup
import time

result = pd.Dataframe()

URL = "https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats"

response = request.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
value = soup.find('td', class="left ")