import requests
from bs4 import BeautifulSoup # 이게 크롤러의 기본이다.
# pip는 라이브러리 설치 시 쓰는 것임. 설치하는 도구구
# 파이썬 라이브러리 설치 명령어: pip install requests
# 파이썬 라이브러리 삭제 명령어: pip uninstall requests

# 크롤러의 기본
# 1. 파이썬으로 데이터가 들어있는 웹사이트에 접속(그럼 HTML이 도착)
data = requests.get("https://finance.naver.com/item/sise.nhn?code=005930") # 이후 변수에 저장(data라고 명명)
print(data) # <Response [200]> 출력됨

# 응답 상태 코드 확인
# print(data.status_code) # 200이면 접속 성공 -> 웹페이지에 접속이 제대로 되고 있나를 확인 가능.

# BeautifulSoup으로 HTML 파싱하기
# data.text: 문자열(str) 형태로 HTML을 가져옴
# data.content: 바이트(bytes) 형태로 HTML을 가져옴
# 두 방식 모두 BeautifulSoup에서 정상적으로 작동합니다. 
# 다만 한글이 포함된 웹페이지의 경우 data.text를 사용하는 것이 더 안전할 수 있습니다.
soup = BeautifulSoup(data.content, 'html.parser') # 이후 변수에 저장(soup라고 명명) -> 이 변수에는 웹페이지의 모든 정보가 들어있음. 이렇게 하면 예쁘게 출력됨.


# 2. HTML 속에서 필요한 정보만 싹 뽑기

# 마우스 우클릭 '검사' -> HTML 속에서 원하는 정보 찾기
# find(): 첫 번째로 일치하는 요소 하나만 찾기
# price_element = soup.find("strong", id="_nowVal")
# print("삼성전자 현재가:", price_element.text)

# 현재가 코드 <strong class="tah p11" id="_nowVal">55,700</strong> 
# 강의 방식 따라가기기
# find_all(): 일치하는 모든 요소를 리스트로 찾기 (강의 방식)
all_price_elements = soup.find_all("strong", id="_nowVal")
# print(all_price_elements[0]) # 첫 번째 요소의 텍스트만 출력 => html 까지 전부 출력됨.
print("삼성전자 현재가:", all_price_elements[0].text)


# 두 번째로, 거래량 찾아보기
# <span class="tah p11" id="_quant">7,794,181</span> 이게 거래량 코드

# all_quant_elements = soup.find_all("span", class_="p11") # 클래스는 예약어이므로, class_로 써야 함!!!!
# 여기서 주의, 클래스에 띄어쓰기가 있으면 안됨. 띄어쓰기 없이 써야 함. 위에 그거는 클래스 2개라는 뜻이므로, 그 중 하나만 써주면 됨. 그렇지 않으면 ㄹㅇ 에러남.

# print("삼성전자 거래량:", all_quant_elements[0].text)
# 여기서 문제가 되는 부분은
# "tah" 클래스만 가진 모든 <span> 태그를 다 가져오고
# 그 중 첫 번째 요소의 텍스트를 출력한다는 점입니다.
# 그런데 네이버 금융의 HTML 구조상
# "tah" 클래스는 현재가, 거래량, 시가, 고가, 저가 등 여러 곳에 반복적으로 사용됩니다.
# 그래서 all_quant_elements[0]은 거래량이 아니라 현재가에 해당하는 태그일 가능성이 높아요.
# 그래서 그냥 나는 id로 찾겠음.
# 클래스로만 찾으면 여러 개의 요소가 리스트로 반환되기 때문에,
# 정확히 몇 번째 인덱스가 거래량인지를 직접 확인해서 인덱스를 지정해야 합니다.

quant_element = soup.find("span", id="_quant")
print("삼성전자 거래량:", quant_element.text)



# 3. 뽑은 정보를 파이썬 변수에 저장
# 4. 저장된 정보를 활용해 원하는 작업 수행

