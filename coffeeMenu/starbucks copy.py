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
filename = f"starbucks-menu_{current_date}.json"

# 웹드라이버 초기화 (Chrome 사용)
browser = webdriver.Chrome()

# 페이지 로드
browser.get('https://www.starbucks.co.kr:7643/menu/drink_list.do')
# print(browser)

# 페이지의 끝까지 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# '더보기' 버튼이 나타날 때까지 기다림 (최대 20초)
# while True:
#     try:
#         # '더보기' 버튼이 나타날 때까지 최대 20초간 대기
#         more_button = WebDriverWait(browser, 5).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, ".line_btn"))
#         )
#         if more_button:
#             more_button.click()  # '더보기' 버튼 클릭
#             print("Clicked '더보기' button.")
#             time.sleep(2)  # 페이지 로딩 대기
#     except Exception as e:
#         print("더보기 버튼을 찾을 수 없음:", e)
#         break  # '더보기' 버튼이 더 이상 없으면 반복문 탈출



# # 업데이트된 페이지 소스를 변수에 저장
html_source_updated = browser.page_source
soup = BeautifulSoup(html_source_updated, 'html.parser')
print(soup)

# # 데이터 추출
starbucks_data = []
tracks = soup.select("#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd > ul > li")
for track in tracks:
    name = track.select_one("#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd > ul > li > dl > dd").text.strip()
    image_url = track.select_one("#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd > div.product_list > dl > dd > ul > li > dl > dt > a > img").get('src')
    starbucks_data.append({
        "li": name,
        "img": image_url
    })

    print(starbucks_data)

#     # 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(starbucks_data, f, ensure_ascii=False, indent=4)

# # 브라우저 종료
browser.quit()