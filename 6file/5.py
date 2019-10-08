fin = open('6file/input5.txt', 'r', encoding='utf8')
s = fin.readlines()
fin.close()

words = (' ').join(s).split()
newStr = ''
count = 0
for line in s:
    for char in line:
        if char.isalpha():
            count += 1
            newStr += char
        else:
            newStr += ' '

print(count, 'letters')
print(len(newStr.split()),'words')
print(len(s.split('\n'))-1, 'lines')
pass
