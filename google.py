from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
#주소 검색
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
#검색창 클릭
elem = driver.find_element_by_name("q")
# 검색창에 입력값
elem.send_keys("꼬부기 포켓몬")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

# 자바스크립트 시작
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 브라우저 끝까지 내린다
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 로딩까지 기다린다
    time.sleep(SCROLL_PAUSE_TIME)

    # 스크롤이 끝까지 내려갔는지 확인 
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # 결과 더보기 클릭
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        #오류나면 멈추기
        except:
            break
    last_height = new_height


# 여러개 elements
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

#이미지 이름 바꾸기 위한 기본설정
count = 1 
for image in images:
    try:
        image.click()
        time.sleep(2)
        # 한개 element
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count += 1
    except:
        pass
driver.close()