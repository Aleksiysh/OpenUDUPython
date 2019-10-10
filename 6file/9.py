fin = open('input9.csv','r',encoding='utf8')
fout = open('out9.csv','w',encoding='utf8')
for line in fin:
    lstLine = line.split(';')
    print(str(int(lstLine[1]))+';'+lstLine[0],file = fout)
fin.close()
fout.close()
