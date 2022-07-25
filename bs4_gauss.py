import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[1].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print(link)
ratings = soup.find_all("div", attrs={"class":"rating_type"} )

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = cartoon.a["href"]
#     print(title, link)

rate = []
for rating in ratings:
    rate.append(float(rating.find("strong").get_text()))

avg = sum(rate) / len(rate)
print(avg)