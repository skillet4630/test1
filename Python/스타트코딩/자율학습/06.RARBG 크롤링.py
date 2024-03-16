# https 주로가 채계적으로 잡혀있는 사이트 크롤링 예
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 결과를 저장할 빈 리스트
titles = []

for num in range(8):
    url = f"https://rargb.to/search/{num}/?search=publicagent%201080p%20x265"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    torrent_links = soup.find_all('a', {'title': lambda x: x and 'Public' in x})

    # 결과를 리스트에 추가
    for link in torrent_links:
        titles.append(link['title'])

# 데이터프레임 생성
df = pd.DataFrame({'Title': titles})

# 결과 파일 경로 설정
output_path = r'C:\Users\kjc46\OneDrive\바탕 화면\컴퓨터 공부\Python\Python\스타트코딩\자율학습\PublicAgent.xlsx'

# Excel 파일로 저장
df.to_excel(output_path, index=False)

# 결과 메시지 출력
print(f"Results saved to: {output_path}")
