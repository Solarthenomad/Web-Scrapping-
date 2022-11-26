import time
from selenium import webdriver

brower = webdriver.Chrome()

#1. 네이버로 이동하기
brower.get("http://naver.com")
#browser.get을 통해서 네이버로 접속한거임 원격으로 
#python
#from selenium import webdriver
#browser = webdriver.Chrome()
#browser.get("http://naver.com")
#element = browser.find_element_by_class_name("link_login")
#element.click()
#browser.back()
#browser.forward()
#browser.refresh()
#browser.back()
#element = browser.fin_element_by_id("query")   #검색창의 id 태그가 query임
#element
#from selenium.webdriver.common.keys import Keys
#element.send.keys("나도 코딩")
#element.send.keys(Keys.ENTER)
#element = browser.browser.find_element_by_tag_name("a")
#element = browser.find_element_by_tag_names("a")
#for e in element:
     #element.get_attribute("href")
     
#browser.close() #현재 탭만 닫아줌 
#brower.quit() #현재탭 뿐만 아니라 모든탭을 다 닫음

#2. 로그인 버튼 클릭하게 하기 
element = browser.find_element_by_class_name("link_login")
element.click()


#3.id,pw 입력하기
brower.find_element_by_id("id").send_keys("trixyblack4")
brower.find_element_by_id("pw").send_keys("banan5215!")
#이렇게 했더니 로그인 오류가 뜸 그러면 새로 입력해야겠지...? 4번한 다음 5번으로 가보자

#4. 로그인 버튼 클릭하기
browser.find_element_by_id("log.login").click()

#3초 있다가 입력하게 하기 
time.sleep(3)

#5. id를 새로 입력하기 
brower.find_element_by_id("id").send_keys("my_id새로입력해주세요")
#근데 이렇게 하면 trixyblack4my_id새로입력해주세요가 나오게됨... 우리는 진짜 새로 입력을 해주고 싶을 뿐임
brower.find_element_by_id("id").clear()
brower.find_element_by_id("id").send_keys("my_id새로입력해주세요")


#6.html 정보 출력해주기
print(brower.page_source)

#7.브라우저 종료해주기
brower.quit()  #전체 브라우저 종료되기
#browser.close() : 현재 탭만 종료해주는 것 













