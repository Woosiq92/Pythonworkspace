'''
score_file = open("score.txt", "w", encoding = "utf8") # score.txt 라는 파일을 쓰기 목적으로 열어서 ( score.txt 파일 생성)
print("수학: 0", file = score_file)
print("영어: 50", file = score_file) # 이내용을 파일에다가 쓰기 
score_file.close()  # 닫기 


score_file = open("score.txt", "a", encoding="utf8")
score_file.write("\n과학 : 80")
score_file.write("\n코딩 : 100") 
score_file.close() 


# 읽기 
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
print(score_file.readline()) # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동 
print(score_file.readline(), end = "") # 줄바꿈 x 
score_file.close() 
'''
# 몇 줄인지 모를때 , 반복문 활용 
score_file = open("score.txt", "r", encoding = "utf8")
while True: 
    line = score_file.readline()
    if not line: 
        break
    print(line, end="")
score_file.close()

# 리스트 활용 
score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # 모든 라인들 
for line in lines: 
    print(line, end="")

score_file.close()
