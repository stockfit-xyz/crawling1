import requests
from bs4 import BeautifulSoup

# 함수 축약해보기
# 데이터 = requests.get("https://finance.naver.com/item/sise.nhn?code=005930")
# soup = BeautifulSoup(데이터.content, 'html.parser')
# print(soup.find_all('strong', id="_nowVal")[0].text)
# print(soup.find_all('span', id="tah")[5].text)

# 정답
# def 현재가() :
#     데이터 = requests.get("https://finance.naver.com/item/sise.nhn?code=005930")
#     soup = BeautifulSoup(데이터.content, 'html.parser')
#     print(soup.find_all('strong', id="_nowVal")[0].text)
#     print(soup.find_all('span', id="tah")[5].text)

# 현재가()

# 위는 삼성전자 건데, 그럼 LG전자도 이렇게 만들 것인가? NO
#그래서 마법의 모자를 만들자. => 구멍 뚫기기
# def 현재가(종목코드) :
#     데이터 = requests.get("https://finance.naver.com/item/sise.nhn?code=" + 종목코드) # 종목코드를 매개변수로 받아서 사용 / 글자 중간에 변수를 넣으려면 {} 사용. 지금 종목코드는 변수이기 때문에 문자가 아닌 변수문법 사용해 주어야. 
#     soup = BeautifulSoup(데이터.content, 'html.parser')
#     print(soup.find_all('strong', id="_nowVal")[0].text)
#     print(soup.find_all('span', id="tah")[5].text)

# 현재가("005930") # 삼성전자
# 현재가("066570") # LG전자
# 정리하자면 함수는 매개변수를 받을 수 있음. 그리고 그 매개변수를 함수 내부에서 사용할 수 있음.
# 더 쉬운 말로 하자면, 구멍을 잘 뚫어놓으면 함수 하나로 다양한 코드를 실행 가능.

# 파알로 정리하기 - 방법 1. return 사용
def 현재가(종목코드):
    데이터 = requests.get("https://finance.naver.com/item/sise.nhn?code=" + 종목코드)  # 종목코드를 매개변수로 받아서 사용 / 글자 중간에 변수를 넣으려면 {} 사용. 지금 종목코드는 변수이기 때문에 문자가 아닌 변수문법 사용해 주어야.
    soup = BeautifulSoup(데이터.content, 'html.parser')
    print(soup.find_all('strong', id="_nowVal")[0].text)
    # 거래량도 참고로 출력
    print(soup.find('span', id="_quant").text)
    return soup.find_all('strong', id="_nowVal")[0].text

현재가("005930") # 삼성전자
현재가("066570") # LG전자

file = open("현재가.txt", "w")
file.write(현재가("005930") + "\n")
file.write(현재가("066570") + "\n")
file.close()

# 퍼알로 정리하기 - 방법 2. 리스트 사용
리스트2 = []
def 현재가2(종목코드):
    데이터 = requests.get("https://finance.naver.com/item/sise.nhn?code=" + 종목코드) # 종목코드를 매개변수로 받아서 사용 / 글자 중간에 변수를 넣으려면 {} 사용. 지금 종목코드는 변수이기 때문에 문자가 아닌 변수문법 사용해 주어야.
    soup = BeautifulSoup(데이터.content, 'html.parser')
    print(soup.find_all('strong', id="_nowVal")[0].text)
    리스트2.append(soup.find_all('strong', id="_nowVal")[0].text)

현재가2("005930") # 삼성전자
현재가2("066570") # LG전자

file = open("현재가2.txt", "w")
file.write(리스트2[0] + "\n") # 리스트 첫번째 요소 출력
file.write(리스트2[1] + "\n") # 리스트 두번째 요소 출력
file.close()

# ---------------
# 숙제 : 다음 종목들의 현재 가격을 모두 txt 파일로 저장하려면?
종목들 = ["005930", "066575", "005380", "035720", "034220", "003490"] # 삼성전자, LG전자, 현대차, 카카오, LG디스플레이, 대한항공


