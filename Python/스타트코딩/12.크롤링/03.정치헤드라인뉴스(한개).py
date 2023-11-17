import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'} # 봇이라고 막혔을경우를 대비
response = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100", headers=header) # headers=header도 마찬가지로 봇이라고 막혔을 경우를 대비
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('.sh_text_headline')
print(title.text.strip()) # .strip() 출력되는 텍스트의 양쪽 공백 제거