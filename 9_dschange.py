# 자료구조의 변경 

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


''' 
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 
추첨 프로그램을 작성핫시오. 

조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정 
조건 2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가 
조건 3: random 모듈의 shuffle 과 sample 활용 

(출력 예제)
-- 당첨자 발표 -- 
치킨 당첨자 : 1 
커피 당첨자 : [2, 3, 4]
-- 축하합니다 -- 
''' 

''' 활용 예제 
from random import shuffle, sample
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1)) # 리스트 중에 1개를 무작위로 뽑기 
''' 

from random import shuffle, sample
users = range(1, 21)
print(users)
users = list(users)
print(users)
shuffle(users)
print(users)
winners = sample(users, 4) # 중복 불가 위해 / 4명 중 1명 치킨, 3명 커피 

print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : {0} ".format(winners[0]))
print("커피 당첨자 : {0} ".format(winners[1:])) 
print("커피 당첨자 : {0}, {1}, {2} ".format(winners[1], winners[2], winners[3])) 
print("-- 축하합니다-- ")



