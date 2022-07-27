import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/shmis/crowling/chromedriver.exe")

for i in range(1,21):
    # 리그 전체가 있는 사이트로 이동
    driver.get("https://fbref.com/en/comps/9/Premier-League-Stats")
    time.sleep(1)

    # 각 클럽을 클릭
    club_btn = driver.find_element(By.XPATH, "//*[@id='results111601_overall']/tbody/tr[{}]/td[1]/a".format(i))
    club_btn.click()
    time.sleep(1)
    # liverpool xpath : //*[@id="results111601_overall"]/tbody/tr[2]/td[1]/a
    # chelsea xpath : //*[@id="results111601_overall"]/tbody/tr[3]/td[1]/a
    # 이런 식임
    



    # with open("1"+"1".csv', 'w') as 

#driver.back() <- 뒤로가기