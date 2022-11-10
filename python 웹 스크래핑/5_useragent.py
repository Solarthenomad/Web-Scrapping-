import requests
#useragent
url = "http://google.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
#useragent를 넣어줌으로서 chrome에 내가 실제로 접속하는(원격으로) 가 가능해진다. 
res = requests.get(url, headers = headers )
#이 페이지(url)에 접속할 때 나의 유저 에이전트 값을 넘겨주는 것이 가능해진다.
#headers안에 useragent값을 받은 headers 를 넘겨줌
res.raise_for_status()
print(res.text)
print(len(res.text))

with open("mynaver.html", "w", encoding="utf8") as f:
    f.write(res.text)
    
    #접속하는 브라우저에 따라서 user agent가 달라짐 