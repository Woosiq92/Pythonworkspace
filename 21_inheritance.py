# 틀만들기 , 일반 유닛 
class Unit: 
    def __init__(self, name, hp): # init : 파이썬 생성자 , 정의 
        self.name = name 
        self.hp = hp 
  
# 공격 유닛 
class AttackUnit(Unit): 
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  # 상속 
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed) 

# 발키리 : 한번에 14발 미사일 발사 공중 공격 유닛 

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
