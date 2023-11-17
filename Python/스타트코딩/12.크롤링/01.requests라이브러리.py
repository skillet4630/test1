# 1.새 파이썬 파일을 만든뒤 새터미널에 pip install requests 입력
# 2.밑에처럼 진행

import requests

response = requests.get("https://www.naver.com")
html = response.text
print(html)