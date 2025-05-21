# 네이버 금융 API를 사용한 주가 크롤링 <- 앞에 app.py가 에러 나서.
import requests  # HTTP 요청을 보내기 위한 라이브러리

# 네이버 금융 API URL (삼성전자 주식 코드: 005930)
# m.stock.naver.com은 네이버 금융의 모바일 API 서버
# /api/stock/005930/basic는 삼성전자의 기본 정보를 가져오는 엔드포인트
url = "https://m.stock.naver.com/api/stock/005930/basic"

# API 호출을 위한 헤더 설정
# User-Agent는 웹 브라우저처럼 보이게 하기 위한 설정
# 일부 API는 브라우저가 아닌 요청을 차단할 수 있기 때문에 필요
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# API 호출 및 데이터 가져오기
# requests.get()으로 GET 요청을 보내고, headers에 위에서 설정한 User-Agent를 포함
response = requests.get(url, headers=headers)
# response.json()으로 JSON 응답을 파이썬 딕셔너리로 변환
data = response.json()

# 현재가 출력
# data 딕셔너리에서 'closePrice' 키의 값을 가져와 출력
print("삼성전자 현재가:", data['closePrice']) 