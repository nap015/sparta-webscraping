from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('./chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=sugsch&w=img&DA=GIQ&sq=tpqmsxls+alsrb&o=1&sugo=1&q=%EC%84%B8%EB%B8%90%ED%8B%B4+%EB%AF%BC%EA%B7%9C") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!
###################################
i=1
thumbnails = soup.select('#imgList > div > a > img')
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'imgs_homework/{i}.jpg')
    i+=1

driver.quit() # 끝나면 닫아주기\