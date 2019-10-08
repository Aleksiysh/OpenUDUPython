fin = open('input3.txt', 'r', encoding='utf8')

for value in fin:
    summ = sum(map(int, value.split()))
    print(summ,end = " ")
    
fin.close()

