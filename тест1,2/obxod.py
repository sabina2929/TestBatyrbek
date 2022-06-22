import os
import pandas as pd
import openpyxl
path = 'C:\\test'
book=openpyxl.Workbook()
sheet=book.active
sheet['A1']='namefile'

def obxodFile(path,level=1,row=2):
    print('Level=',level,'content',os.listdir(path))
    for i in os.listdir(path):
        if os.path.isfile(path+ '\\' + i):
            sheet[row][0].value = i
            row += 1
            print('только файлы',i)
        elif os.path.isdir(path + '\\' + i):
            print('следующая папка',path + '\\' + i)
            obxodFile(path + '\\' + i,level+1)
            print('возвращаемся', path)



obxodFile(path)

book.save("m.xlsx")