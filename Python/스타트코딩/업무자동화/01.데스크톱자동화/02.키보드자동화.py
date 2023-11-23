import pyautogui
import pyperclip # 모듈 : 누군가 만들어 놓은 파이썬 코드

# 1.키보드 입력(문자) [pyautogui라이브러리는 한글지원 안함]
pyautogui.write('startcoding', interval=0.25)

# 2.키보드 입력(키)
pyautogui.press('enter')

# 3.키보드 입력(여러개 동시)
pyautogui.hotkey('ctrl', 'c') # 복사하기

# 4.한글 입력 방법
pyperclip.copy('한글입력')
pyautogui.hotkey('ctrl', 'v')