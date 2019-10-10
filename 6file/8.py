# def mykey(x):

dictTmp = {}
fin = open('input8.csv','r',encoding='utf8')
for line in fin:
    record = line.split(';')
   # print(record[0],int(record[1]))
    if record[0] not in dictTmp:
        dictTmp[record[0]]= [0,0] 
    dictTmp[record[0]][0]+=1
    dictTmp[record[0]][1]+=int(record[1])    
fin.close() 
listRes= list()
for record in dictTmp:
    line = [dictTmp[record][1]/dictTmp[record][0],record]
    listRes.append(line)
listRes.sort()
fout = open('out8.txt','w',encoding='utf8')
for value in listRes:
    print(value[1],file = fout)

fout.close()   
pass