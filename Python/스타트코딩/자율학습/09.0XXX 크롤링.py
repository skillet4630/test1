# https 주로가 채계적으로 잡혀있지 않는 사이트 크롤링 예
import requests
import pandas as pd # pip install pandas
from bs4 import BeautifulSoup



header = {'User-agent' : 'Mozila/2.0'} # 봇이라고 막혔을경우를 대비
response = requests.get("https://0xxx.me/index.php?s=PublicAgent%201080p&next=2258", headers=header) # headers=header도 마찬가지로 봇이라고 막혔을 경우를 대비 #페이지 넘길때 마다 주소 바꿔주기
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('a.screenshot') # titles로 하면 리스트를 가져옴 #커서 가져다 가면 a.screenshot 나옴

# 텍스트를 저장할 빈 리스트 생성
text_list = []

# 텍스트를 리스트에 추가
for title in titles:
    text_list.append(title.text.strip())

# 데이터프레임 생성
df = pd.DataFrame({'Title': text_list})

# Excel 파일로 저장
output_path = r'C:\Users\kjc46\OneDrive\바탕 화면\컴퓨터 공부\Python\Python\스타트코딩\자율학습\PublicAgent(8).xlsx'
df.to_excel(output_path, index=False)

print(f"Titles saved to: {output_path}")
    
