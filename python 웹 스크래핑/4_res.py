#주민등록번호
#901201-111111
#abcdef-111111


#이메일 주소 
#solarthenoamd@gmail.com
#solarthenoamd2@gmail.com

#차량 번호 
#11가 1234
#123가 1234


#IP주소 
#192.168.0.1 

#각각의 데이터들의 형식들이 다름 - 이 형식들을 체크할 수 있는 방법 = 정규식 

import re 
#abcd, book, desk처럼 4글자짜리 

#p = re.compile(어떤 정규식을 컴파일 할지)
p = re.compile("ca.e") #. : 하나의 문자를 의미 care, cafe, case등을 출력해주는데 caffe는 안됨. 
# ^de : 문자열의 시작 desk, destination 출력되나 fade는 안됨(뒤에 나오자나)
# se$ : 문자열의 끝 case, base 가능한데 face는 안됨 


    
m =p.match("case") #m은 불린값(참, 거짓)을 가지게 된다.
#매치가 되지 않으면 에러가 발생한다. 
if m:
    print(m.group())
    #매칭되면 매칭된 그룹정보를 출력해주면 됨
else : 
    print("매칭되지 않음")
    
    
##다른 방법으로 하기. class를 만들어서 인자를 넣어보자 
def print_match(m):
    if m:
        print(m.group()) #group은 일치하는 문자열을 반환해주는 것이다. #입력받은 문자열을 출력해주는 것
        print(m.string) #입력받은 문자열 출력해줌
        print(m.start()) #일치하는 문자열의 시작 index
        print(m.end()) #일치하는 문자열의 끝 index
        print(m.span()) #일치하느 문자열의 시작과 끝 index
        
        
    else :
        print("매칭되지 않음")
m = p.match("니가 매칭되는지 확인해주고 싶은 단어 넣어봐")
print_match(m)

##위랑 똑같음

m = p.search("good care")
#search : 주어진 문자열 중에 일치하는게 있는지 확인하는 것
#true flase 값을 가지게 됨  
print_match(m)

lst = p.findall("careless") #findall은 일치하는 모든 것을 리스트 형태로 반환하는 것이다. 
print(lst)


#1. p = re.compile("원하는 형태로 ")
#2. m = p.match("비교할 문자열 넣어줘서 매칭되는지 확인") : 주어진 문자열의 처음부터 일치하는지 확인해주기 
#3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인한다. 
#4. lst = p.findall("good care cafe(비교할 문자열)") #findall : 일치하는 모든 것들을 리스트 형태로 출력함
#print(lst)

#원하는 형태 : 정규식 


 
