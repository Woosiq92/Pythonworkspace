# super : 자식 클래스에서 부모클래스의 내용을 사용하고 싶을경우 사용


class Unit: 
    def __init__(self): 
        print("Unit 생성자")

class Flyable: 
    def __init__(self): 
        print("Flyable 생성자")
    
class FlyableUnit(Flyable, Unit): 
    def __init__(self): 
        #super().__init__() // 맨 처음에 상속 받는 클래스에 대해서만 init 함수가 호출 되어서 
        Unit.__init__(self) # 모든 부모 함수의 초기화를 할때는 각각 모두 초기화 
        Flyable.__init__(self)

#드랍십 
dropship = FlyableUnit() 