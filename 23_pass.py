# 틀만들기 , 일반 유닛 
class Unit: 
    def __init__(self, name, hp, speed): # init : 파이썬 생성자 , 정의 
        self.name = name 
        self.hp = hp 
        self.speed = speed 

    def move(self, location): 
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
  
# 공격 유닛 
class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)  # 상속 
        self.damage = damage # Unit 외  추가 요소 
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage): 
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("체력 {0}, 공격력 {1} \n".format(self.hp, self.hp))
        if self.hp <= 0: 
            print(" {0} : 파괴되었습니다. ".format(self.name))

# 날수 있는 기능을 가진 클래스 
class Flyable:
    def __init__(self, flying_speed): 
        self.flying_speed = flying_speed

    def fly(self, name, location): 
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스 
class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속 
    def __init__(self, name, hp, damage, flying_speed): 
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed  = 0 
        Flyable.__init__(self, flying_speed)

    def move(self, location): # move 재정의 
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물 
class BuildingUnit(Unit): 
    def __init__(self, name, hp, location): 
        pass # 아무것도 안하고 일단 넘어감 

#서플라이 (인구수) 
supply_depot = BuildingUnit("서플라이디폿", 500, "7시")
