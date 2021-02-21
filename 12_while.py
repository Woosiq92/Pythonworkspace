#while

customer = "토르"
person = "unknown"
index = 5 
while index >= 1: 
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer, index))
    index -= 1 
    if index == 0: 
        print("커피는 폐기 처분되었습니다.")

while person != customer: 
    print("{0}, 커피가 준비되었습니다. ".format(customer))
    person = input("이름이 어떻게 되세요? ")

