# 1.승패여부
# 2.챔피언 이름
# 3.킬
# 4.데스
# 5.어시스트

# 변수를 사용할 때
result = '승리'
champ_name = '비에고'
kill = 13
death = 9
assist = 17

# 리스트 사용할 때
play_data = ['승리', '비에고', 13, 9, 17]
play_data2 = ['승리', '비에고', 13, 9, 17]

# 딕셔너리 사용할 때
play_data = {
    'resutlt' : '승리',
    'champ_name' : '비에고',
    'kill' : 13,
    'death' : 9,
    'assist' : 17
}

### 딕셔너리 수정하는 방법 ###
# 기존 값 변경
play_data['resutlt'] = '패배'

# 새로운 키, 값 추가
play_data['level'] = 18

# 데이터 삭제
del play_data['champ_name']