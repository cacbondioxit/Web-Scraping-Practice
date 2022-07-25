import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/shmis/crowling/chromedriver.exe")

for i in range(1,21):
    driver.get("https://fbref.com/en/comps/9/Premier-League-Stats")
    time.sleep(1)

    # 테이블 긁어오는 코드 작성

    time.sleep(1)`

# liverpool xpath : //*[@id="results111601_overall"]/tbody/tr[2]/td[1]/a
# chelsea xpath : //*[@id="results111601_overall"]/tbody/tr[3]/td[1]/a

# with open("Liverpool"+'.csv', 'w') as 