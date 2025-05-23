import requests
from bs4 import BeautifulSoup

data = requests.get("https://m.search.naver.com/search.naver?sm=mtb_hty.top&ssc=tab.m_blog.all&oquery=%EA%B2%B8%EC%86%90%EC%9D%80%ED%9E%98%EB%93%A4%EB%8B%A4&tqi=ju838dqVWfZssf6GKVVssssstho-015158&query=%EB%B0%95%EC%A7%80%EC%84%B1&ackey=wdxrztzn")

print(data.content) # 이 데이터를 파싱해서 원하는 데이터를 추출해야 함. 잘 담겨있는지 확인

soup = BeautifulSoup(data.text.replace("\\", ""), "html.parser") #예쁘게 파싱해줌

print(soup)

# 블로그 제목 추출
#<a href="https://m.blog.naver.com/diaspora0709/223873608533" class="title_link" data-cb-trigger="" data-cb-target="90000003_00000000000000341FE82B55" onclick="return goOtherCR(this,&quot;a=blg*a.nblg&amp;r=1&amp;i=90000003_00000000000000341FE82B55&amp;u=&quot;+urlencode(this.href))">유로파리그 결승전 기념 토트넘 맨유 - 이영표 vs <mark>박지성</mark> (2006/07 EPL)</a>
titles = soup.find_all('a', class_='title_link')
for title in titles:
    print(title.text) # 블로그 제목만 추출

# 브라우저 주소창은 GET 요청을 보내는 곳이다.
# GET 요청한 데이터에 .text하면 데이터가 문자열로 나옴.

# 다른 데이터 수집도 해보기

ydata = requests.get('https://m.search.naver.com/search.naver?sm=mtb_hty.top&ssc=tab.m_blog.all&oquery=%EB%B0%95%EC%A7%80%EC%84%B1&tqi=ju%2Fw6wpr46ZssU3arclssssstWV-175751&query=%EC%9C%A0%EC%9E%AC%EC%84%9D&ackey=7m0k4i5w')
ysoup = BeautifulSoup(ydata.text.replace("\\", ""), "html.parser")
ytitles = ysoup.select('a.title_link')
print(ytitles)
print(len(ytitles))
print(ytitles[0].text)
print(ytitles[0].get('href'))

print(ytitles[1].text)
print(ytitles[1].get('href'))

print(ytitles[2].text)
print(ytitles[2].get('href'))

# 이런 식으로 쭉 해본다.

