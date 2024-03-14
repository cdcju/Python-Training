#write to a cell
from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['A1'] = 1
sheet['C2'] = 13
sheet.cell(row=2, column=2).value = 2

book.save('write2cell.xlsx')