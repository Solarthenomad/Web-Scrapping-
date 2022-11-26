from selenium import webdriver
import time

#로딩하는 것 기다리기 위한 모듈 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#위에 있는 expected_conditions 모듈 이름 ㅈㄴ 길어서 ec로 축약해줬음 까먹지 말기 

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()  #가는 날 선택 버튼 클릭해주자


#이번 달 27일, 28일 선택
browser.find_elements_by_link_text("27")[0].click()
#27 두개인데 이중에서 첫 번째 선택하는 것
browser.find_elements_by_link_text("28")[0].click()

#다음 달 27, 28일 선택해주기
browser.find_elements_by_link_text("27")[1].click()
#27 두개인데 이중에서 첫 번째 선택하는 것
browser.find_elements_by_link_text("28")[1].click()

#이번달 27일 다음 달 28일 선택해주기 
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()

#도착지를 제주도로 선택해주기 
#개발자 도구에서 오른쪽 버튼 누르면 xpath 복사하기가 나움
browser.find_element_by_xpath("//*[@id ='recommendationList']/ul/li[1]")

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id = 'content']/div[2]/div/div[4]/ul/li[1]"))
#어떤 element가 도달할 떄까지 10초동안 기다려 줘 

#첫 번째 결과 출력 
element = browser.find_element_by_xpath("//*[@id = 'content']/div[2]/div/div[4]/ul/li[1]")
print(element.text)





