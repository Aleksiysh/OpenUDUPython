import openpyxl
vedomost = list()
for i in range(1,1001):
    fileName = '../rogaikpyta/'+str(i)+'.xlsx'
    wb = openpyxl.load_workbook(fileName)
    sheet = wb.active
    record = (sheet['B2'].value+' ' +str(sheet['D2'].value))
    vedomost.append(record)
    #print(i)

vedomost.sort()
fout = open('out13.txt','w',encoding='utf8')
for value in vedomost:
    print(value,file = fout)
fout.close()

pass