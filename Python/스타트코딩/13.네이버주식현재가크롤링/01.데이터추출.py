### 결과물 ###
# 네이버 증권 웹사이트에서 현재가를 크롤링해서 엑셀에 저장
# 자신의 주식 종목 분석에 활용할 수 있음

### 준비물 ###
# 파이썬 기초 문법(변수, 리스트, 반복문)
# 크롤링 기초(request, BeautifulSoup)

### 실습순서 ###
# 네이버 증권 사이트 현재가 데이터를 파이썬으로 가져온다.
# 엑셀을 불러와서 데이터 저장

import requests
from bs4 import BeautifulSoup

# 종목 코드 리스트
codes = [
    '005930', # 삼성전자
    '000660', # SK하이닉스
    '035720'  # 카카오
]

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',', '')
    print(price)