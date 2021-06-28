from openpyxl import load_workbook
wb = load_workbook("sample4.xlsx")
ws = wb.active

# 번호 영어 수학

a1 = ws["A1"] # 번호
b1 = ws["B1"] # 영어
c1 = ws["C1"] # 수학

# A열의 너비를 5로 설정
ws.column_dimensions["A1"].width = 5

wb.save("sample_style.xlsx")