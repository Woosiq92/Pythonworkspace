# 추가 .. 숫자 처리 함수 

print(abs(-5))				# 5(절대값)
print(pow(4, 2))			# 16(pow(a, b) - a의 b제곱)
print(max(1, 4))			# 4(숫자 중 최대값)
print(min(1, 4))			# 1(숫자 중 최소값)
print(round(2.11))			# 2(반올림)
print(round(2.78))			# 3

from math import floor, ceil, sqrt 
'''
from math import * -> Unused wildcard import 오류 발생 
너무 쓸데 없이 많은 함수 가져옴 
-> 필요한 함수만 import 하면 좋겠다 . 
''' 
print(floor(4.99)) # 내림 
print(ceil(4.99)) # 올림 
print(sqrt(16)) # 제곱근  

# 랜덤 함수 

from random import random, randrange, randint

print((random())) # 0.0 이상 ~ 1.0 미만의 임의의 값을 생성 


# Quiz ) 0.0 ~ 10.0 임의의 값을 생성하려면? 
print(random() * 10 )  

print(int(random() * 10))  # int -> 정수형 출력
print(int(random() * 10) + 1 )  # 1부터 

# Quiz) 로또 번호 생성기 

print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)
print(int(random() * 45 ) + 1)

print(randrange(1,46)) # 랜덤 함수 범위 설정 함수 : 1 ~ 46 미만의 임의의 값 생성 

print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성 , 함수에 커서 갖다 대서 설명 읽기 


'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들엇습니다 
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다 

아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오. 

조건 1 : 랜덤으로 날짜를 뽑아야함. 
조건 2 : 월별 날짜는 다름을 감안하여 당월의 최소 일수는 28이내로 정함 .
조건 3 : 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외 

출력문 : 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다. 
'''
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) +" 일로 선정되었습니다.")



