fin = open('6file/input6.txt', 'r', encoding='utf8')
s = fin.readlines()
fin.close()

maxLen = 0
for line in s:
    if len(line) > maxLen:
        maxLen = len(line)
for line in s:
    if len(line) == maxLen:
        print(line)

pass