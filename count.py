# not finished yet 2018-11-23

import xlrd
import numpy

# 设置路径
path = 'E:/2. NaRi/1. My NaRi Projects/1. neo4j/alert2(1).bak.xlsx'
workbook = xlrd.open_workbook(path)
Data_sheet = workbook.sheets()[0]  # 通过索引获取
rowNum = Data_sheet.nrows  # sheet行数
colNum = Data_sheet.ncols  # sheet列数

# 获取所有单元格的内容
list = []
for i in range(rowNum):
    rowlist = []
    for j in range(colNum):
        rowlist.append(Data_sheet.cell_value(i, j))
    list.append(rowlist)

# delete operation
arr = numpy.delete(list, 0, axis = 0)
arr = numpy.delete(arr, [1,2], axis = 1)
Arr = []
for i in range(len(arr)):
    Arr.append(arr[i])

print(Arr)

l1 = ['a123',1,'c','b',2,'b','c','d','a']
l2= sorted(set(l1),key=l1.index)
print('l2:',l2)
print('l1:',l1)

#输出
#l2: ['a', 1, 'c', 'b', 2, 'd']
#l1: ['a', 1, 'c', 'b', 2, 'b', 'c', 'd', 'a']
#