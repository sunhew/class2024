import requests as req
from bs4 import BeautifulSoup as bs    ##가져온 문서를 읽기 편하게 정리해주는 코드
import pandas as pd    ##데이터 정리

res = req.get("https://music.bugs.co.kr/chart")            ##가져올 사이트 지정


# print(res.text)
# print(res.status_code)  ##200   200대에서는 대부분 정보가 가져와짐

soop = bs(res.text, "lxml")
# print(soop)

## 선택한 데이터 가져오기
ranking = soop.select(".ranking > strong")
title = soop.select(".title > a")
artist = soop.select(".artist > a:nth-child(1)")  


# print(len(ranking))
# print(len(title))
# print(len(artist))            ##데이터 갯수 확인

## 선택한 데이터 저장
# rankingList = []
# titleList = []
# artistList = []

# for i in range(len(ranking)) : 
#     rankingList.append(ranking[i].text)
#     titleList.append(title[i].text)
#     artistList.append(artist[i].text)

# print(artistList)
    
# data = {"ranking" : rankingList, "title" : titleList, "artist" : artistList}
# print(pd.DataFrame(data))



## 파이손 스타일로 코드 짜기

## 데이터 저장
rankingList = [r.text.strip() for r in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]

# 데이터 프레임 생성
chart_df = pd.DataFrame({
    'RankingList' : rankingList,
    'TitleList' : titleList,
    'ArtistList' : artistList
})

# JSON 파일로 저장
chart_df.to_json("busChart100.json", force_ascii=False, orient="records")