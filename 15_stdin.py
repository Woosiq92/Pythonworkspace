print("python", "java", "javascript", sep = " vs ")

print("python", "java", "javascript", sep = " , ", end =" ? ") # end = 문장의 끝부분을 줄바꿈이 아닌 물음표로 바꿔라 
print("무엇이 더 재밌을까요? ")

# import sys 
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr) 

# 시험 성적 
scores = { "수학" : 0, "영어": 50, "코딩":100}
for subject, score in scores.items(): 
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":") # ljust : 왼쪽으로 정렬하고 8칸 띄기


# 은행 대기 순번표 
# 001, 002, 003, ... 
for num in range(1, 4): 
    print("대기 번호 : " + str(num).zfill(3)) # 총 3공간 확보 , 값이 없으면 0으로 채우기 

answer = input("아무 값이나 입력하세요 : ") # 기본 문자열 형태로 저장 
print("입력하신 값은 " + answer + " 입니다.")
