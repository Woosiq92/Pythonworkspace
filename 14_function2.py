# 온라인 뱅킹 만들기 
def open_account(): 
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금 
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.". format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: 
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다. ".format(balance - money)) 
        return balance - money
    else: 
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원 
    return commission, balance - money - commission

balance = 0 # 잔액 
balance = deposit(balance, 1000)
print(balance) 

balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1}원입니다.".format(commission, balance))

# 함수의 기본 값 설정 

def profile(name, age, main_lang): 
    print("이름 : {0}\t 나이: {1} \t 주 사용 언어:{2}" \
        .format(name, age, main_lang)) # 줄바꿈 \ 

profile("유재석", 20, "파이썬 ")

# 같은 학교 같은 학년 같은 반 같은 수업 이면 중복하여 값 입력할 필요 없음. 
def profile1(name, age = 17, main_lang= "파이썬"): 
    print("이름 : {0}\t 나이: {1} \t 주 사용 언어:{2}" \
        .format(name, age, main_lang)) # 줄바꿈 \ 
    
profile1("유재석")

# 호출 순서 
def profile2(name, age, main_lang):
    print(name, age, main_lang)

profile2(main_lang = "자바", age = 25, name = "유재석")

# 가변 인자 ( 서로 다른 변수 개수 입력할 떄 )
def profile3(name, age, lang1, lang2, lang3, lang4, lang5): 
    print("이름 : {0} \t 나이 : {1} \t".format(name, age), end = "") # end -> 줄바꿈 없이 끝 
    print(lang1, lang2, lang3, lang4, lang5)

profile3("유재석", 20, "python", "java", "c", "c++", "c#")
profile3("김태호", 25, "Kothlin", "Swift", "", "", "")

## * 사용 
def profile4(name, age, *language): 
    print("이름 : {0} \t 나이 : {1} \t".format(name, age), end = " ") # end -> 줄바꿈 없이 끝 
    for lang in language: 
        print(lang, end = " ")
    print()

profile4("유재석", 20, "python", "java", "c", "c++", "c#")
profile4("김태호", 25, "Kothlin", "Swift", "", "", "")

# 지역변수와 전역 변수 

gun = 10 # 전역 변수 

def checkpoint(soldiers): # 경계 근무 
    gun = 20 # 지역 변수 
    # global gun # 전역 공간에 있는 gun 사용 
    gun = gun - soldiers
    print("함수 내 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers): # 경계 근무 
    gun = gun - soldiers
    print("함수 내 남은 총 : {0}".format(gun))
    return gun 

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감 
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("전체 총 : {0}".format(gun))

''' 
Quiz) 표준 체중을 구하는 프로그램을 작성하시오. 
* 표준 체중 : 각 개인의 키에 적당한 체중 
(성별에 따른 공식) 
남자 : 키(m) x 키 (m) x 22 
여자 : 키(m) x 키 (m) x 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산 
       * 함수명 : std_weight
       * 전달값 : 키(height, 성별(gender))
조건 2 : 표준 체중은 소수점 둘째자리까지 표시 

( 출력 예제 )
키 175cm 남자의 표준 체중은 67.38kg 입니다. 
'''

def std_weight(height, gender):
    if gender == "남": 
        return height * height * 22
    elif gender == "여": 
        return  height * height * 21
    
    
height = 175 
gender = "남"
weight = round(std_weight(height /100 , gender), 2) # round 2 -> 소수점 둘째 짜리 

print(" 키 {0}cm {1}의 표준 체중은 {2}kg 입니다. ".format(height, gender, weight))