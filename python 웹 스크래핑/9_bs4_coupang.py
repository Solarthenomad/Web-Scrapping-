import requests
from bs4 import BeautifulSoup


url = ""
headers={"User-agent" : ""}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
print(res.text)

items = soup.find_all("li", attrs= {"class":re.complie("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    
    #광고 제외
    
    ad_badge = item.find("span", attrs = {"class":"ad-badge-text"})
    if ad_badge:
        print("광고 상품 제외합니다.")
        continue #광고 상품 나오는 거 끝날 때까지ㅇ 위의 코드를 현실화하고 다음으로 넘어감
    
    name = item.find("div", attrs={"class" : "name"}).get_text()#제품명
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    #가격
    #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회하기
    rate = item.find("em", attrs={"class":"rating"}).get_text()
    if rate:
        rate.get_text()
    else:
        print("평점 없는 상품을 제외합니다.")
        continue
    #평점 수
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}).get_text()
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() #이렇게만 하면 (26) (7) 이렇게만 출력됨...
        rate_cnt = rate_cnt[1:-1]  #양옆의 괄호들을 잘라주고(슬라이싱) 숫자만 순수하게 출력해줌
        print("리뷰 수", rate_cnt)
    else:
        print("평점 수 없는 상품을 제외합니다.")
        continue
    
    if float(rate) >= 4.5 and rate_cnt:
        print(name, rate, price, rate_cnt)
        
    
    
    
    
    #광고가 붙은 부분은 제외를 하도록 한다. 내가 긁어온 페이지에 광고가 붙은 것들...
    
    #span태그가 붙은 것들이 광고라는 것을 확인 가능
    
    
    
