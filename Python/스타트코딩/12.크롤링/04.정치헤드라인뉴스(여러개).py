import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'} # 봇이라고 막혔을경우를 대비
response = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100", headers=header) # headers=header도 마찬가지로 봇이라고 막혔을 경우를 대비
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.sh_text_headline') # titles로 하면 리스트를 가져옴
for title in titles:
    print(title.text.strip())