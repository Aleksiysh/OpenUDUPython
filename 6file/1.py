fin = open('input1.txt', 'r', encoding='utf8')
mySet = set()
count = 0
for value in fin:
    mySet.update(set(value.split()))
    
fin.close()

print(len(mySet))