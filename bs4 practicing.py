import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
rank01 = soup.find(attrs={"class":"rank01"})
# print(rank01.a.get_text())

# print(rank01.find_next_siblings("li"))

webtoon = soup.find("a", text="참교육-90화")

print(webtoon)