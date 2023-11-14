# 1. 결과값이 없는 함수
def printName(name):
    print(name)
    
printName("스타트코딩")

# 2. 매개변수가 없는 함수
import random

def getRandomNumber():
    number = random.randint(1,10)
    return number

print(getRandomNumber())

# 3. 결과값과 매개변수가 없는 함수
def sayHi():
    print("안녕하세요")
    
sayHi()