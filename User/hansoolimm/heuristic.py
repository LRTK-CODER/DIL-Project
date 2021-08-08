import pandas as pd
import openpyxl

wb = openpyxl.load_workbook('test.xlsx', data_only=True)

sheet =  wb.active
for a in range(5):
   sheet.cell(row=a+2, column=3).value = '홍길동'

wb.save('test.xlsx')
    
print(wb)
