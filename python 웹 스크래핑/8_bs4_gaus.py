import requests
from bs4 import BeautifulSoup

url = ""
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs = {"class" : "title" })
#첫번째 화 출력해보기
title = cartoons[0].a.get_text()
print(title)
#첫 번쨰 화의 link(href) 출력해보기
#a["href"] a의 href 클래스 출력
link = cartoons[0].a["href"]
print("http://comic.naver.com" + link)

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = cartoon.a["href"]
    link_href = "http://comic.naver.com" + link
    print(title, link)

#평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class" : "rating_type"})

for cartoon in cartoons:
    rate =cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
    print("전체점수 : ", total_rates)
    print("평균점수 :", total_rates/len(cartoons))