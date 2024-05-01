from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import json

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"coffeebanhada-menu_{current_date}.json"

# 웹드라이버 초기화 (Chrome 사용)
browser = webdriver.Chrome()

# 로드해야 하는 여러 링크
urls = [
    'https://coffeebanhada.com/main/menu/list4.php?page_type=1'
]
# print(urls)
# 데이터 추출을 위한 빈 리스트 생성
coffeebanhada_data = []

for url in urls:
    # 페이지 로드
    browser.get(url)
    
    # 페이지의 끝까지 스크롤 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 업데이트된 페이지 소스를 변수에 저장
    html_source_updated = browser.page_source
    soup = BeautifulSoup(html_source_updated, 'html.parser')

    # 데이터 추출
    tracks = soup.select("#wrap > div.sub_content.menu_wrap > .menu_lst.m_menu_lst")
    for track in tracks:
        name = track.select_one("#wrap > div.sub_content.menu_wrap > div > div > p").text.strip()
        image_url = track.select_one("#wrap > div.sub_content.menu_wrap > div > div > div > img").get('src').replace('/data', 'https://coffeebanhada.com/data')

        coffeebanhada_data.append({
            "p": name,
            "img": image_url
        })

# # # 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(coffeebanhada_data, f, ensure_ascii=False, indent=4)

# 브라우저 종료
browser.quit()