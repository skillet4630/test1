#원하는 사이트를 기입하도록 함
#사이트내 원하는 정보를 크롤링함
#크롤링한 정보를 가지고 다음주소로 넘어가서 또 크롤링함
#계속 반복하다가 원하는 정보가 안나오면 멈춤
try:
    driver.find_element_by_css_selector(".comp").click()
except:
    break