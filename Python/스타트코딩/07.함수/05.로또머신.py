#1.로또 번호 6개를 생성
#2.로또 번호는 1~45까지의 랜덤한 번호
#3.6개의 숫자 모두 달라야 한다
#4.로또 번호 생성함수를 작성하고 사용한다
import random 

def getRandomNumber():
    number = random.randint(1,45)
