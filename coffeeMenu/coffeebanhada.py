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
import os

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
folder_path = "coffeebanhada"
filename = f"{folder_path}/menucoffeebanhada_{current_date}.json"

# 폴더 생성
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 웹드라이버 초기화 (Chrome 사용)
options = ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# 페이지 로드
browser.get('https://coffeebanhada.com/main/menu/list4.php?page_type=1')

# '더보기' 버튼이 나타날 때까지 기다림 (최대 20초)
while True:
    try:
        more_button = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".line_btn"))
        )
        if more_button:
            more_button.click()  # '더보기' 버튼 클릭
            print("Clicked '더보기' button.")
            time.sleep(2)  # 페이지 로딩 대기
    except Exception as e:
        print("더보기 버튼을 찾을 수 없음:", e)
        break

# 업데이트된 페이지 소스를 변수에 저장
html_source_updated = browser.page_source
soup = BeautifulSoup(html_source_updated, 'html.parser')

# 데이터 추출
coffeebanhada_data = []
tracks = soup.select("#wrap > div.sub_content.menu_wrap > .menu_lst.m_menu_lst")
for track in tracks:
    name = track.select_one("#wrap > div.sub_content.menu_wrap > div > div > p").text.strip()
    image_url = track.select_one("#wrap > div.sub_content.menu_wrap > div > div > div > img").get('src')
    if not image_url.startswith('http'):
        image_url = 'https://coffeebanhada.com' + image_url

    coffeebanhada_data.append({
        "p": name,
        "img": image_url
    })

# 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(coffeebanhada_data, f, ensure_ascii=False, indent=4)

# 브라우저 종료
browser.quit()