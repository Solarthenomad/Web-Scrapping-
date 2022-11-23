    #지금까지 한 페이지만 했는데 이번에는 여러 페이지에 있는 정보들을 긁어고자 함 => url의 페이지를 바꿔줄 필요가 있음 
    
import requests
from bs4 import BeautifulSoup

for i in range(1,6): #page들 수 1~6
    
    print("페이지",i)
    

    url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"


    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup= BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")})
    
    #print(items[0].find("div", attrs = {"class" : "name"}).get_text())
    
    for item in items :
        
        #광고 붙은 상품들은 충분한 평가를 받지 못하여 신뢰가 잘 안됨. 그래서 신뢰도를 위해서 광고 제품들을 제외 시켜주기 
        
        
        
                
        ad_badge = item.find("span", attrs = {"class" : "ad-badge-text"})
        if ad_badge:
            print("<광고 상품 제외합니다.>")
            continue #이 제품을 제외하고 그냥 다음 단계로 넘어간다.
        #리뷰 100개 이상, 평점 4.5이상 되는 것들만 골라내기 
        
        if float(rate)>= 4.5 and int(rating_number) >=100 :
            #rate를 실수 형태로 바꿔주자
            
            print(name, price, rate, rating_number)
            
        
        name = items.find("div", attrs = {"class" : "name"}).get_text()
        
        #애플 제품 제외해주기 
        
        if "Apple" in name:
            print("<Apple 상품 제외합니다>")
            continue
        
        #상품 이름명들을 가져오기 
        #가격 
        price = items.find("strong", attrs = {"class" : " price-value"} ).get_text()
        
        #평점
        
        
        
        
        
        
        rate = items.find("em", attrs = {"class" : "rating"}).get_text()
        #근데 평점이 없는 애들은 어떡하지...? 출력하지 말아야겠지!! 
        
        if rate: #평점이 존재할 때 그냥 if 변수라고 조건문 적기 
            rate = rate.get_text()
            
        else : 
            rate = "평점없음"
            print("<평점 없는 상품 제외합니다>")
            continue
        #평점수 
        rating_number = items.find("span" , {"class" : "rating-total-count"}).get_text()
        
        if rating_number:
            rating_number = rating_number.get_text()
            rating_number = rating_number[1:-1] #맨 뒷쪽 앞까지의 수와 맨 첫번째수만 슬라이싱해서 출력함
            print("리뷰 수", rating_number)
        else : 
            rating_number = "평점 없음"
            print("<평점 수 없는 상품 제외합니다>")
            continue
        
        print(name, price, rate, rating_number)
        
        