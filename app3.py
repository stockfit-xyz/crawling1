# 웹크롤러 두번째 시간
# Case 1: 글자가 해체되어 있는 경우
# 예시: 삼성전자 현재가: 55,700원 이라고 하면, 5/5/7/0/0 이렇게 나옴.
# 이 경우 공통 클래스를 찾아서 출력하면 됨.

import requests
from bs4 import BeautifulSoup

# 네이버 금융 삼성전자 페이지에서 HTML 가져오기
response = requests.get("https://finance.naver.com/item/sise.nhn?code=005930")
soup = BeautifulSoup(response.content, 'html.parser')

# 현재가가 들어있는 em 태그 안의 span 태그(class='blind')를 찾기
# 아래 코드처럼 써도 됨.
# price_span = soup.find('em', class_='no_down').find('span', class_='blind')
# print("삼성전자 현재가:", price_span.text)

em_tags = soup.find_all('em', class_='no_down')
price_span = em_tags[0].find('span', class_='blind')
print("삼성전자 현재가:", price_span.text)

# Case 2: class, id가 하나도 없는 경우
# 예시: 우측 하단에 동일업종 등락률 <em>-0.34%</em> 이렇게 나옴.
# 방법 1 : 이 경우 태그 이름을 찾아서 출력하면 됨.
print(soup.find_all('em')[0].text) # 인덱스로 위치 지정정
print(soup.find_all('span', class_ = "tah")[5].text)

# 방법 2 : 이 경우 select 함수를 사용하면 됨. select() => css 슬렉터
soup.select(".tah")
# css 상에서 class는 . 으로 표시되고, id는 # 으로 표시됨. 태그명은 그냥 이름만 쓰면 되고, 둘다 만족하려면 붙여쓰면 됨. 내부 요소일 경우 띄어쓰기로 구분
# 둘다 만족하는 거 예시 : soup.select(".tah#up")


# Case 3 : 이미지 수집
# <img id="img_chart_area" src="https://ssl.pstatic.net/imgfinance/chart/item/area/day/005930.png?sidcode=1747843516261" width="700" height="289" alt="이미지 차트" onerror="this.src='https://ssl.pstatic.net/imgstock/chart3/world2008/error_700x289.png'">
# find_all 함수 써도 되고 .select 함수 써도 됨.
이미지 = soup.select('#img_chart_area')[0]
print(이미지) # 이 때는 태그가 전체적으로 출력됨

# 이제 src를 통해서 실제 이미지를 수집한다.
# 위에서 수집한 요소에서 src 속성을 찾아서 출력하면 됨.
print(이미지['src'])


# Case 4 : 다른 종목 주가 가격도 동시에 수집
lg_data = requests.get("https://finance.naver.com/item/main.naver?code=066570")
soup = BeautifulSoup(lg_data.content, 'html.parser')
print("lg 현재가 : ", soup.find_all('strong', id="_nowVal")[0].text)
print("lg 거래량 : ", soup.find_all('span', id="tah")[5].text)

# 종목 주가 시각화 예시 : https://finance.naver.com/item/sise_day.nhn?code=005930&page=1


# URL과 종목코드 매핑시켜서 가져오면 쉽다