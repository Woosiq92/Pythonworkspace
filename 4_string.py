sentence = '파이썬' 
print(sentence)
sentence2 = "파이썬은 쉬워요 "
print(sentence2)
sentence3 = """  
나는 파이썬이 , 
쉬워요 
"""  # 총 네줄 출력 ( 줄바꿈 포함 )
print(sentence3)

# 슬라이싱 

woosik = "920308-1234567" # 리스트, 인덱스 개념 필요 

print("성별 : " + woosik[7] )
print("년도 : " + woosik[0:2]) # 범위 개념 필요  , 0 ~ 2 직전 까지 
print("월 : " + woosik[2:4])
print("일 : " + woosik[4:6])
print("생년 월일 : " + woosik[0:6])
print("생년 월일 : " + woosik[:6]) # 처음부터 6 직전까지 
print("뒤 7자리 : " + woosik[7:14])
print("뒤 7자리 : " + woosik[7:]) # 7 부터 끝까지 
print("뒤 7자리 : " + woosik[-7:]) # 맨뒤에서 7부터 끝까지 

#문자열 처리 함수 

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 대문자 확인 
print(len(python))
print(python.replace("Python", "java"))

index = python.index("n")
print(index) # n의 인덱스 번호 

index = python.index("n", index + 1) # 6번째 부터 탐색 
print(index)

print(python.find("n"))
print(python.find("java")) # 포함되어 있지 않으면 -1 반환 
# print(python.index("java")) # index함수로 찾으면 원하는 값이 없으면 오류 발생 

print(python.count("n"))

# 띄어쓰기를 통해 서로 다른 문자열 합치기 
print("a" + " b")
print("a"," b")

# 그외 다양한 문자열 포맷 방법 
print(" 나는 %d살 입니다. " % 20 )
print(" 나는 %s을 좋아해요." % "파이썬")
print(" Apple 은 %c로 시작해요 " % "A")

print(" 나는 %s살 입니다. " % 20 )
print(" 나는 %s과 %s을 좋아해요." % ("파란", "빨간"))

print(" 나는 {}살 입니다.".format(20))
print(" 나는 {}과 {}을 좋아해요.".format("파란", "빨간"))
print(" 나는 {0}과 {1}을 좋아해요.".format("파란", "빨간"))
print(" 나는 {1}과 {0}을 좋아해요.".format("파란", "빨간"))


print(" 나는 {age}살이며, {color}을 좋아해요.".format(age = 20, color = "빨간"))


# 파이썬 3. 6~ 부터 가능 
age = 20 
color = "빨간" 
print(f"나는 {age}살이며, {color}을 좋아해요.")

# 탈출 문자 

# - 줄바꿈 하고 싶을 때 
print("백문이 불여일견 \n 백견이 불여일타")

# - 큰따옴표 사용하고 싶을 떄 \"", \'
print('저는 "최우식"입니다.')
print("저는 \"최우식\"입니다. ")

# \\ : 문장내에서 \ 하나로 인식 - 경로 지정시 
print("C:\\Users\\~")

# \r : 커서를 맨앞으로 이동 
print("Red Apple\rPine") # 처음으로 가서 Pine 4개의 공간만큼 채움 

#\b : 백스페이스 ( 한글자 삭제 )
print("Red\bApple")

# \t : 탭 

'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오 
예 ) http://naver.com 
규칙 1 : http:// 부분은 제외 => naver.com 
규칙 2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver
규칙 3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성 

예시 ) 생성된 비밀번호 : nav51! 
출력문 : print("{0}의 비밀 번호는 {1} 입니다.".format(url, password))
'''
url = "http://naver.com" # google, youtube 등등 바꿔보기.. 
a = url.replace("http://", "") # 규칙 1 
print(a) 

a = a[:a.index(".")] # a의 문자열 중에서 .의 위치 직전까지 자르기 
# a[6:a.index(".")]
print(a)

password = a[:3] + str(len(a)) + str(a.count("e")) + "!"
print("{0}의 비밀 번호는 {1} 입니다.".format(url, password))
