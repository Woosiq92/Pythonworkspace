# 집합 ( set )
# 중복 안됨, 순서 없음 

my_set = {1, 2, 3, 3, 3}
print(my_set) # 중복 허용 안함 

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 ( java 와 python 을 모두 할수 있는 사람 )
print (java & python )
print(java.intersection(python))

# 합집합 (java or python 중 하나라도 할 수 있는 사람 )
print(java | python )
print(java.union(python))

# 차집합 (java만 할 수 있는 사람) 
print(java - python )
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남 
python.add("김태호")
print(python) 

# java 를 잊었어요 
java.remove("김태호 ")
print(java)