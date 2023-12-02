import openpyxl
from openpyxl.styles import Font, Side, Border, Alignment

save_path = 'Python/스타트코딩/업무자동화/03.엑셀자동화/total.xlsx'

# 기존의 엑셀 파일 불러오기
wb = openpyxl.load_workbook(save_path)

# 시트 선택
ws = wb['data']

# 열 너비 변경
wb.code_dimensions['a'].width = 20

# 행 높이 변경
ws.row_dimensions[1].height = 30

# 저장
wb.save(save_path)
