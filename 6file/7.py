fin = open('6file/input7.txt', 'r', encoding='utf8')
s = fin.read()
fin.close()
fout = open('6file/out7.txt', 'w', encoding='utf8')
print(s[::-1], file=fout)
fout.close()