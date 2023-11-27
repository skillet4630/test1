# 새터미널에 pip install webdriver_manager 설치
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주로 이동
driver.implicitly_wait(5) # 웹페이지가 로딩 될때 까지 5초 기다림
driver.maximize_window() # 화면 최대화
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("kjc4630")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("Dltnstls1")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()
time.sleep(2)

# 메일함 이동
driver.get("https://mail.naver.com/v2/folders/0/all")
time.sleep(2)

# 메일 쓰기 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write > span").click()
time.sleep(2)

# 받는사람
driver.find_element(By.CSS_SELECTOR, "#recipient_input_element").send_keys("//받는사람//")
time.sleep(2)

# 제목
driver.find_element(By.CSS_SELECTOR, "subject_title").send_keys("//셀레니움만으로 자동화 하기//")
time.sleep(2)

driver.switch_to.frame("")
# 본문
driver.find_element(By.CSS_SELECTOR, "workseditor-content").send_keys("잘 될까요?")
time.sleep(2)

# 보내기
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task").click()