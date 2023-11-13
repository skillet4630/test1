#프로그램 사용자로부터 가방과 시계의 금액을 입력받는다.
#조건에 따라 합계 금액을 계산하고, 합계금액을 출력한다.
#1.합계금액이 10만원 이상이면 할인률 30%
#2.합계금액이 5만원이상 10만원 미만이면 할인률 20%
#3.합계금액ㅇ 5만원 미만이면 할인률 10%

bag_price=int(input("가방 금액을 입력하시오>>>"))
watch_price=int(input("시계 금액을 입력하시오>>>"))

total_price=bag_price+watch_price

if total_price >= 100000:
    print("합계금액은 :", total_price * 0.7)
elif total_price >= 50000:
    print("합계금액은 :", total_price * 0.8)
else:
    print("합계금액은 :", total_price * 0.9) 