import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

url = "https://search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

items = soup.find_all("div", attrs={"class":"wrap_cont cont_type2"})

for item in items[:5]:
    title = item.find("a", attrs={"class":"tit_main"}).get_text()
    rate = item.find("em", attrs={"class":"rate"}).get_text()
    rate = float(rate)
    rate_cnt = item.find("a", attrs={"class":"link_count"}).get_text()[:-4]
    date = item.find_all("dd", attrs={"class":"cont"})[0].get_text()
    accum = item.find_all("dd", attrs={"class":"cont"})[1].get_text()
    link = item.find("a", attrs={"class":"tit_main"})["href"]

    print(title, rate, rate_cnt, date, accum, "https://search.daum.net/search"+link)
