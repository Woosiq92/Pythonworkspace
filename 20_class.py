'''
# 마린 
name = "마린"
hp = 40 
damage = 5 

print("{0} 유닛이 생성되었습니다. ". format(name))
print("체력 {0}, 공격력 {1} \n".format(hp, damage))

#탱크 

tank_name = "탱크"
tank_hp = 150 
tank_damage = 35 

print("{0} 유닛이 생성되었습니다. ". format(tank_name))
print("체력 {0}, 공격력 {1} \n".format(tank_hp, tank_damage))

def attack(name, location, damage): 
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
'''

# 틀만들기 , 일반 유닛 
class Unit: 
    def __init__(self, name, hp, damage): # init : 파이썬 생성자 , 정의 
        self.name = name # 멤버 변수 : 클래스 내에서 정의된 변수 
        self.hp = hp 
        self.damage = damage
        print("{0} 유닛이 생성되었습니다. ". format(self.name))
        print("체력 {0}, 공격력 {1} \n".format(self.hp, self.damage))
# 똑같은 클래스를 통해서 서로 다른 객체 생성 
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35 ) # 매개변수 숫자 맞춰야 오류 발생 x 

# 공격 유닛 

class AttackUnit: 
    def __init__(self, name, hp, damage):
        self.name = name # 멤버 변수 : 클래스 내에서 정의된 변수 
        self.hp = hp 
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage): 
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("체력 {0}, 공격력 {1} \n".format(self.hp, self.hp))
        if self.hp <= 0: 
            print(" {0} : 파괴되었습니다. ".format(self.name))

# 파이어뱃 
firebat1 = AttackUnit("파이어뱃", 50, 16 )
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)