cabinet = {3: "유재석", 100:"김태호"}
print(cabinet[3]) # 3번 열쇠를 가지고 있는 사람 
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 값이 없으면 실행 오류 
print(cabinet.get(5)) # None 출력 
print(cabinet.get(5, "사용 가능")) 
print("hi")

print ( 3 in cabinet ) # True 
print ( 5 in cabinet ) # False 

# 키는 숫자일 필욘ㄴ 없음 
a = {"A-3": "유재석", "B-100":"김태호"}
print(a["A-3"])
print(a["B-100"])

# 새손님 
a["C-20"] = "조세호"
a["A-3"] = "김종국" # 덮어쓰기 
print(a)

# 나간 손님 
del a["A-3"]
print(a)

print(a.keys()) # 키들만 출력 
print(a.values()) # 값들만 출력 
print(a.items()) # 둘다 출력 
a.clear()  # 초기화 
print(a)

