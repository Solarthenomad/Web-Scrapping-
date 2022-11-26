import requests 
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
           "Accept-Language" : "ko-KR,ko"}
#Accept-Language는 내가 받고 싶은 언어권의 페에지를 요청하는 것이 가능해진다. 

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text , "lxml")

movies = soup.find_all("div", attrs = {"class" : "ImZGtf mpg5gc"})
print(len(movies))

#with open("movie.html", "w", encoding="utf8") as f:
    #f.write(res.text)
   # f.write(soup.prettify())
    #html 문서를 예쁘게 출력해주느 것이 prettify이다.
 
    
    #구글 무비에서는 접속하는 user agent정보를 통해서 서로 다른페이지를 리턴시켜줌. 예를 들어서 사용자 각각에게 해당되는 맞춤형 알고리즘이라던가 나라별로 다른 페이지에 들어갈 수 있도록 함 
    
for movie in movies:
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
    print(title)
    
    
    
    
    
    
     