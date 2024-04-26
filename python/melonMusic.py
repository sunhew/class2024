import requests as req
from bs4 import BeautifulSoup as bs    ##가져온 문서를 읽기 편하게 정리해주는 코드
import pandas as pd    ##데이터 정리

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
res = req.get("https://www.melon.com/chart/index.htm", headers=head)

# print(res.text)
# print(res.status_code)  ##406   400대는 대부분 정보가 불러와지지않음

soop = bs(res.text, "lxml")

# 선택한 데이터 가져오기
ranking = soop.select("tbody .wrap.t_center > .rank")
title = soop.select("tbody .wrap_song_info .ellipsis.rank01 span > a")
artist = soop.select("tbody .wrap_song_info > .ellipsis.rank02 span > a:nth-child(1)")

# print(len(artist))

# 데이터 저장
rankingList = [r.text.strip() for r in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]

print(artistList)

# 데이터 프레임 설정
chart__meln = pd.DataFrame({
    'Ranking' : rankingList,
    'Title' : titleList,
    'Artist' : artistList
})

# JSON파일 저장
chart__meln.to_json("MelonChart.json", force_ascii=False, orient="records")