# 새터미널에 pip install pyautogui
import pyautogui 
import time

# 1.화면 크기 출력(출력되는 단위를 넘어서면 안됨)
print(pyautogui.size())

# 2.마우스 위치 출력
time.sleep(2) # 너무 빨라서 딜래이 넣어주기
print(pyautogui.position())

# 3.마우스 이동
pyautogui.moveTo(41, 442, 2) # 2초동안 천천히 움직이기

# 4.마우스 클릭
pyautogui.click() # 좌클릭
pyautogui.click(button='right') # 우클릭
pyautogui.doubleClick() # 더블클릭
pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다 실행

# 5.마우스 드래그(마우스정보 활용)
pyautogui.moveTo(41, 442, 2)
pyautogui.drag(539, 80, 2)