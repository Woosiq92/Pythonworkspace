
# 변수 실습 전 변수의 개념 ( 저장 설명 )
# 변수 
# 자기소개 
# 주석 개념 설명 
''' 이렇게 하면 
여러 문장 주석 
처리 가능 
'''
# 여러 문장 선택후 ( ctrl + / )  -> 일괄적으로 주석 
print("나의 이름은 ㅇㅇ이에요")
print("나이는 4살이며, 취미는 독서입니다.")
print("저는 어른일까요? True")

name = "ㅊㅇㅅ"
age = 20
hobby = "독서"
is_adult = age >= 20 

print("나의 이름은 " , name , "이에요")
print("나이는 ", age ," 이며, 취미는",hobby,"입니다.")  
print("저는 어른일까요? " , is_adult)


print("나의 이름은 " + name + "이에요")
print("나이는 "+ str(age) +" 이며, 취미는 "+ hobby + " 입니다.") # 정수형을 문자형으로 변환 - str 
print("저는 어른일까요? " + str(is_adult))


'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오. 
변수명 : station, station1, station2 

변수값 : 공덕, 애오개, 홍대 순서대로 입력 

출력 문장 : xx 행 열차가 들어오고 있습니다. 

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
'''

number = 2 + 3 * 4 
print(number)

number = number + 2
print(number)

number += 2  # +, - ,* ,/, %  
print(number)

number *= 2 
print(number)


