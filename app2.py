# 크롤러 예제 2 - 앞에 게 나는 빈 값이길래. 커서가 알려준 셀레니움 사용해봄봄
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome 드라이버 설정
driver = webdriver.Chrome()
driver.get("https://finance.naver.com/item/sise.nhn?code=005930")

# 페이지가 로드될 때까지 더 오래 대기
time.sleep(5)

try:
    # 차트 영역 안의 현재가를 표시하는 정확한 위치를 가리킴
    # CSS 선택자 설명:
    # #chart_area: id가 'chart_area'인 요소
    # > : 바로 아래 자식 요소를 선택
    # div.rate_info: class가 'rate_info'인 div 태그
    # p.no_today: class가 'no_today'인 p 태그
    # em: em 태그
    # span.blind: class가 'blind'인 span 태그
    # 이 선택자는 차트 영역 안의 현재가를 표시하는 정확한 위치를 가리킴
    price_element = driver.find_element(By.CSS_SELECTOR, "#chart_area > div.rate_info > div > p.no_today > em > span.blind")
    print("삼성전자 현재가:", price_element.text)
except Exception as e:
    print("주가를 찾을 수 없습니다:", e)

# 브라우저 종료
driver.quit() 