import openpyxl
import statistics as st
from random import seed
from random import randint

book = openpyxl.load_workbook('numbers.xlsx', data_only=True)

sheet = book.active

rows = sheet.rows
seed(1)
for i in range(1,26):
    sheet['A'+str(i)] = randint(56 ,200)
book.save('numbers.xlsx')
values = []

for row in rows:
    for cell in row:
        values.append(cell.value)

print("Number of values: {0}".format(len(values)))
print("Sum of values: {0}".format(sum(values)))
print("Minimum value: {0}".format(min(values)))
print("Maximum value: {0}".format(max(values)))
print("Mean: {0}".format(st.mean(values)))
print("Median: {0}".format(st.median(values)))
print("Standard deviation: {0}".format(st.stdev(values)))
print("Variance: {0}".format(st.variance(values)))