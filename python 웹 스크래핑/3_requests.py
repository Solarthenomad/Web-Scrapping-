import requests

res = requests.get("http://naver.com")
print("응답코드:" ,res.status_code) #200이면 정상적으로 http://naver.com의 정보를 받아서 res에 저장된 것이다. 

if res.status_code == requests.codes.ok: #200이랑 똑같으면
    print("정상입니다.")

else:
    print("문제가 생겼습니다. [에러 코드", res.status_code,"]")
    
res.raise_for_status()
#문제가 없다고 하면 출력해주고 문제가 있다고 하면 에러코드를 띄어줌
print("웹 스크래핑을 진행합니다.")
print(len(res.text))
print(res.text)
#res의 text(긁어온 것들)을 터미널로 출력해준다. 그리고 그 출력한 것을 mynaver.html에 넣어준다. 

with open("mynaver.html", "w", encoding = "uft-8") as f:
    f.write(res.text)
