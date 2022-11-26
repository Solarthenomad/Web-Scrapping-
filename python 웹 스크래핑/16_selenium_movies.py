from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

#지정한 위치로 스크롤 내리기
browser.execute_script("window.scrollTo(0,1080)")
#윈도우에서 스크롤을 세로 방향으로만 1080만큼 내리라는 얘기임 

browser.execute_script("window.scrollTo(0,2080)")



#화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#2초에 한 번씩 스크롤을 내리는 작업을 하게 됨 
interval = 2

#현재 문서 높이를 가져와서 저장한다. 
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복 수정
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("return document.body.scrollHeight")
    
    #페이지 로딩 대기하기
    time.sleep(interval)
    
    #현재 문서 높이를 가져와서 저장하기 
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height == prev_height:
        break
    
    
    prev_hegiht = current_height 
    
    print("스크롤 완료")
    
    
    
    






