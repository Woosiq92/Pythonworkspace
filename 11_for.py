# 매번 코드 칠 필요 x 

for waiting_num in [0, 1, 2, 3, 4]:
    print("대기번호: {0}".format(waiting_num)) 

for waiting_num in range(5):
    print("대기번호: {0}".format(waiting_num)) 

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer)) 

# 한줄 for 
# 출석 번호가 1, 2, 3, 4 ... 앞에 100을 붙이기로 함 -> 101, 102, 103, 104 
students = list(range(1, 6))
print(students)
students = [ i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환 
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환 
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)