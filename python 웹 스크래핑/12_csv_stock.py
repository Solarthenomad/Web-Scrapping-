#네이버 금융 

import csv
import requests
import re
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f= open(filename, "w", encoding="utf8" newline="")
writer = csv.writer(f)

for page in range(1,5):
    
    res = requests.get(url + str(page) )
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all()
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: #의미없는 데이터는 skip하고 다른 조건의 데이터들만 출력할 수 있도록 함
            continue
        data = [column.get_text() for column in columns]
        #print(data)
        writer.writerow()
    