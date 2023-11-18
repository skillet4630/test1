import requests
from bs4 import BeautifulSoup
import pyautogui # 터미널에 pip install pyautogui 설치

keyward = pyautogui.prompt("검색어를 입력하세요")
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyward}") # f스트링
html = response.text

soup = BeautifulSoup(html , 'html.parser')
links = soup.select(".news_tit") # 결과는 리스트
for link in links:
    title = link.text # 태그 안에 텍스트요소를 가져온다
    url = link.attrs['href'] # href의 속성값을 가져온다(외워놓기)
    print(title, url)