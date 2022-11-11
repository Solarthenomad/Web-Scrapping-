import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text,"lxml")
#네이버 웹툰 전체 목록 가져오기 
cartoons = soup.find_all("a", attrs = {"class":"title"})
#soup 전체에서 a 태그 중 class가 title인 모든 a태그 내용들을 가져온다. 

#class 속성이 title인 모든 "a" element를 반환한다. 
for cartoon in cartoons:
    print(cartoons.get_text())
    

 