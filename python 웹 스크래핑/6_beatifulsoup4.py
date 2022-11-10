import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
#"네이버 웹툰 url 넣어서 긁어올거임"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#res에 있는 것들을 파스어(lxml)를 통해서 객체soup를 만듦 soup안에 모든 정보들이 다있음 
print(soup.title) #title 출력
print(soup.title.get_text()) #title에서 태그들을 떼고 순수 텍스트만 출력해줘
print(soup.a) #soup 객체 안의 a태그를 출력하는데 첫 번째 a 태그를 출력해줘
print(soup.a.attrs) #이 a태그가 가지고 있는 속성 출력 
print(soup.a["href"])
print(soup.a["onclick"])

#이런 친구들은 내가 이 페이지에 대한 이해도가 높고 비교적 페이지가 복잡하지 않을 때 사용이 가능하다. 

soup.find("a", attrs = {"class" : "Nbtn_upload"})
#a 태그 중 class = "Nbtn_upload"인 어떤 element를 찾아줘

#print(soup.find("li", attrs = {"class":"rank01"}))
#이걸 rank1안에다가 넣어줘서 간단하게 쓰자 
rank1 = print(soup.find("li", attrs = {"class":"rank01"}))
print(rank1.a.get_text())
#next_sibling은 rank1의 형제 태그
print(rank1.next_sibling) #여기선 아무것도 출력이 안되
print(rank1.next_sibling.next_sibling)
#여기서 출력이 됨...? 
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
print(rank1.parent) #parent 태그를 출력해줌
rank1.find_next_sibling( "li")
#rank1 태그 기준으로 li인 같은 위치의 태그들만 찾음
rank2 = rank1.find_next_sibing("li")
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
prit(rank2.a.get_text())

rank1.find_next_siblings("li")
#같은 계통의 li태그들을 모두 가져옴 

webtoon = soup.find("a", text= "독립일기-11화 밥공기 딜레마")
print(webtoon)




