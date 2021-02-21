absent = [2, 5] # 결석 
no_book = [7] # 책을 깜빡했음 

# 결석자 제외하고 학생 출석 부르기 
for student in range(1, 11): 
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))


''' 
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다. 
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오. 

조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다. 
조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다. 

(출력문 예제 )
[o] 1번째 손님 ( 소요시간 : 15분)
[ ] 2번째 손님 ( 소요시간 : 50분)
[o] 3번째 손님 ( 소요시간 : 5분)
... 
[ ] 5번째 손님 ( 소요시간 : 15분)

총 탑승 승객 o분 
''' 
from random import randrange
count = 0 
for i in range(1, 51): # 승객 
    time = randrange(5, 51)
    if 5 <= time <= 15: 
        print("[O] {0}번째 손님 ( 소요시간 : {1}분)".format(i, time))
        count += 1
    else: # 매칭 실패 
        print("[ ] {0}번째 손님 ( 소요시간 : {1}분)".format(i, time))
        
print("총 탑승 승객 : {0} 분".format(count))