#프로그램 사용자로부터 자연수를 입력 받고,
#0부터 자연수까지의 합계를 출력하세요.

num=int(input("자연수를 입력하시오>>>"))

sum = 0

for i in range(1, num + 1):
    sum = sum + i

print(sum)