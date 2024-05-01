from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import json

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"theventi-menu_{current_date}.json"

# 웹드라이버 초기화 (Chrome 사용)
browser = webdriver.Chrome()

# 로드해야 하는 여러 링크
urls = [
    'https://www.theventi.co.kr/new2022/menu/all.html?mode=1',
    'https://www.theventi.co.kr/new2022/menu/all.html?mode=2',  
    'https://www.theventi.co.kr/new2022/menu/all.html?mode=3',  
    'https://www.theventi.co.kr/new2022/menu/all.html?mode=4',  
    'https://www.theventi.co.kr/new2022/menu/all.html?mode=5',
    'https://www.theventi.co.kr/new2022/menu/all.html?mode=6' 
]
# print(urls)
# 데이터 추출을 위한 빈 리스트 생성
theventi_data = []

for url in urls:
    # 페이지 로드
    browser.get(url)
    
    # 페이지의 끝까지 스크롤 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 업데이트된 페이지 소스를 변수에 저장
    html_source_updated = browser.page_source
    soup = BeautifulSoup(html_source_updated, 'html.parser')

    # 데이터 추출
    tracks = soup.select("#contents > div > div > div.menu_list > ul > li")
    for track in tracks:
        name = track.select_one("#contents > div > div > div.menu_list > ul > li > a > div.txt_bx > p.tit").text.strip()
        image_url = track.select_one("#contents > div > div > div.menu_list > ul > li > a > div.img_bx > img").get('src').replace('/uploads', 'http://www.theventi.co.kr/uploads')

        theventi_data.append({
            "p.tit": name,
            "img": image_url
        })

# # 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(theventi_data, f, ensure_ascii=False, indent=4)

# 브라우저 종료
browser.quit()