def mykey(x):
    return x[0]

fin = open('input2.txt', 'r', encoding='utf8')
dct = {}
for line in fin:
    lst = list(line.split())
    for word in lst:
        if word not in dct:
            dct[word] = 1
        else:
            dct[word] += 1
fin.close()

lst = list()
for word in sorted(dct):
    rec = (dct[word], word)
    lst.append(rec)
sortLst = sorted(lst,reverse=True,key=mykey)
# for rec in sorted(lst, reverse=True, key=mykey):
#     print(rec[1],end=" ")

pass    


