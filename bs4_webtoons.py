import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# 네이버 웹툰 전체 목록 가져오는 코드
cartoons = soup.find_all("a", attrs={"class":"title"})
# a element의 class 속성이 title인 모든 a 태그가 감싸는 문자열 출력
for cartoon in cartoons:
    print(cartoon.get_text())
