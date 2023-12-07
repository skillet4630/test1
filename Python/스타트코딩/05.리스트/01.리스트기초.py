# 리스트 생성하기
animals = ["사자", "호랑이", "고양이", "강아지"]

# 데이터 접근하기
name = animals[3] # 0번부터 순서대로

# 데이터 추가하기
animals.append("하마") # append() : 리스트 마지막에 요소 추가
animals.append(1) # 잘 쓰이지 않음

# 데이터 삭제하기
del animals[-1] # 마지막 1번 부터 역순으로 제거

# 리스트 슬라이싱
slicing = animals[1:3] # slicing : 연속적인 객체들에(예: 리스트, 튜플, 문자열) 범위를 지정해 선택해서 객체들을 가져오는 방법 및 표기법을 의미합니다. 일부분을 복사해서 가져온다고 생각하면 됩니다.

# 리스트 길이
length = len(animals)

# 리스트 정렬
animals.sort(reverse=True) #sort() 오름차수 정렬 / sort(reverse=True) 내림차수 정렬

print(animals)