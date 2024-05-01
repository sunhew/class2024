from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json

# 웹드라이브 설치(수동)
# brower = webdriver.Chrome()
# brower.get("https://www.music-flo.com/brower")

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"caffebene-menu_{current_date}.json"

# 웹드라이버 초기화 (Chrome 사용)
browser = webdriver.Chrome()

# 페이지 로드
browser.get('http://canbus.kr/doc/menu1.php')
print(browser)

# 페이지의 끝까지 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# # 업데이트된 페이지 소스를 변수에 저장
html_source_updated = browser.page_source
soup = BeautifulSoup(html_source_updated, 'html.parser')
print(soup)

# # 데이터 추출
canbus_data = []
tracks = soup.select("#pageWrap > ul > li")
for track in tracks:
    name = track.select_one("#pageWrap > ul > li > p").text.strip()
    image_url = track.select_one("#pageWrap > ul > li > img").get('src').replace('/uploads', 'http://www.caffebene.co.kr/uploads')
    canbus_data.append({
        "p": name,
        "img": image_url
    })

    print(canbus_data)

# #     # 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(canbus_data, f, ensure_ascii=False, indent=4)

# # 브라우저 종료
browser.quit()