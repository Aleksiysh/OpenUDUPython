min = float('inf')
res = list()

fin = open('input11.csv','r',encoding='utf8')
listProduct = list(fin.readline().split(';'))
for line in fin:
    record = list(line.split(';'))
    for i in range(1,len(record)):
        if min >int(record[i]):
            res.clear()
        if min >=  int(record[i]):
            magazin = record[0]
            product = listProduct[i]
            res.append((magazin,product))    
            min = int(record[i])
res.sort()
print(res[0][1]+res[0][0])
fin.close()
pass