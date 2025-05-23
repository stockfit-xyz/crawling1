import requests
from bs4 import BeautifulSoup

# 무한 스크롤 데이터 수집 1(네이버 블로그)
# 보통의 웹사이트들은 페이지를 넘길 때 마다 새로운 페이지를 로드함 => 페이지가 구분되어 있음.
# 네이버 블로그는 무한 스크롤 형식으로 되어 있음 => 무한 스크롤 형식은 페이지가 구분되어 있지 않음.

# 보통은 URL을 어떻게 바꿔야 페이지가 변하는지 알면 쉽게 크롤링 할 수 있음.

# 기본 형태
# requests.get("첫째 페이지 URL")
# 정보를 거르기
# requests.get("둘째 페이지 URL")
# 정보를 거르기

# 추가 데이터를 달라고 네이버 서버에 요청을 하는 게 답.

# 네이버에서 끝까지 내리다가 보면, 계속 추가가 됨. 즉, 이 페이지를 보여주기 위해서 서버에서 받아온 모든 파일들을 다 보여줌.
# 여기서 더보기 데이터를 찾아라.
# 더보기 데이터가 담긴 파일을 찾은 후 그걸 서버에 따로 요청하면 크롤링 가능.

# 네트워크탭 우측 하단의 Header 탭에서 request URL로 GET 요청을 보내면 이 데이터를 크롤링할 수 있다는 뜻.

# GET요청을 실제로 해보자
# 파이썬으로 웹사이트를 접속하려면 request.get() 함수를 사용함.
response = requests.get('https://m.search.naver.com/search.naver?sm=mtb_hty.top&ssc=tab.m_blog.all&oquery=%EA%B2%B8%EC%86%90%EC%9D%80%ED%9E%98%EB%93%A4%EB%8B%A4&tqi=ju838dqVWfZssf6GKVVssssstho-015158&query=%EB%B0%95%EC%A7%80%EC%84%B1&ackey=wdxrztzn') # 이게 GET 요청 response에 저장

print(response.text) # 이 요청을 보내면 네이버 서버에서 데이터를 줌.

# 두 번째 요청도 보내보기
response2 = requests.get("https://s.search.naver.com/p/review/49/search.naver?abt=%5B%7B%22eid%22%3A%22PWL-PND-PLC%22%2C%22value%22%3A%7B%22bucket%22%3A%223%22%2C%22is_control%22%3Afalse%7D%7D%2C%7B%22eid%22%3A%22PWC-AD-LABEL2%22%2C%22value%22%3A%7B%22bucket%22%3A%223%22%2C%22for%22%3A%22impression-neo%22%2C%22is_control%22%3Afalse%7D%7D%5D&ac=1&api_type=7&aq=0&enlu_query=IggCADKDULgxAAAAuGDqbIuW1YP0vEg6kPSZvPFwEQrNRTpuEhwPenhcakHpHhKhEGqKzjcgEXovbEcj2xJ6lQqOBHSP2Wl7vz%2BusMsoJ2EYHFTOyiLJn0kKHetH%2FrkFqaeLNAmFtwrQ5%2FxySf%2FJA9z21%2Fl47fn0ve5LhShtdtFAMzWaESqwr1n3kQVA2x%2BzN7TP8ntrvjkNUUWBjIvIcllO8gSXUNpOFDk8xW4yXF5%2FAtxG949AhSjXLjqbcDyH836Az4TkTKD4G0MLEJGkveEEK6S7fIHe%2FWFGPEvZ6G%2Bz5o4bLwsb6lkWG%2B5ti3zvy8PEY3ZZJqi6GkyZdjnvJ%2Fd0S57cxZ4ks%2FJmgIv5uJ5ArXh7GfzSn9z8aRUZkDKv4BCSN764ysI88Iq59S2yvDpdPNW6%2BMhaiIfobg%3D%3D&enqx_theme=IggCAGuCULj2AAAAh%2FDtntZaiMLGh3DOFtIyq6lDy02dRCO85PtB2wdufWR0luuEawq1G1VF68dQ2l7wMKsNgewPTM%2FRUNSsDD80dF5JvSLDzwsusC1eBcV7IBc%3D&equery=IggCACSCULgBAAAA12yIlObtl1TOFm94r7mMOw%3D%3D&fgn_city=&fgn_region=&lgl_lat=37.602194&lgl_long=126.929825&lgl_rcode=09380102&ngn_country=KR&nso=&nx_and_query=&nx_search_query=&nx_sub_query=&prank=120&query=%EB%B0%95%EC%A7%80%EC%84%B1&sm=mtb_hty.top&spq=1&ssc=tab.m_blog.all&start=121")

# 이 요청을 보내면 네이버 서버에서 데이터를 줌.
# 이 데이터를 파싱해서 원하는 데이터를 추출해야 함.

# 사실 브라우저 주소창에 URL을 박아도 GET 요청을 보내는 것과 똑같다.