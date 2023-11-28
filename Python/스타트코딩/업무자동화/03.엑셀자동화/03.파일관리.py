import openpyxl

save_path = 'Python/스타트코딩/업무자동화/03.엑셀자동화/거래처A매입현황.xlsx'

# 기존 엑셀 파일 불러오기
wb = openpyxl.load_workbook(save_path)

# 활성화된 시트 선택
ws = wb.active

# 데이ㅓ 추가


# 엑셀 저장
wb.save(save_path)