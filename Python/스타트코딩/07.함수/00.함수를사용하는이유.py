# 함수를 사용하지 않은 경우
print("안녕하세요, 동준님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요, 현식님")
print("현재 프리미엄 서비스 사용기간이 15일 남았습니다.")

print("안녕하세요, 원준님")
print("현재 프리미엄 서비스 사용기간이 7일 남았습니다.")

# 함수를 사용한 경우
def print_message(name, date):
    print("안녕하세요.", name, "님")
    print("현재 프리미엄 서비스 사용기간이 ", date, "일 남았습니다.")
    
print_message("동준", 30)
print_message("현식", 30)
print_message("원준", 30)