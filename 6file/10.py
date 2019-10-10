fin = open('input10.csv','r',encoding='utf')
record = fin.readline()
minval = float('inf')
for record in fin:
    lstRec =sorted(list(map(int,record.split(';')[1::])))
    if lstRec[0]<minval:
        minval = lstRec[0]

print(minval)