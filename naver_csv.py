import csv
import requests
from bs4 import BeautifulSoup

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="cp949", newline="")
writer = csv.writer(f)

for page in range(1,5):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="+str(page)    
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    
    if page == 1 :
        data_header = soup.find("table", attrs={"class":"type_2"}).find("thead").find_all("th")
        title = [tr.get_text().strip() for tr in data_header]
        writer.writerow(title)

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: 
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)
