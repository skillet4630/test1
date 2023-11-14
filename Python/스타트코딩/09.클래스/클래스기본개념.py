# class : 제품의 기본 설계도
class Monster:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f'나는 {self.name} {self.age}살임')
      
# 객체 = 클래스 이름()  
shark = Monster('상어', 7)
wolf = Monster('늑대', 3)

# 객체.메서드() #'.'은 '~의'로 해석하는게 좋음
shark.say()
wolf.say()