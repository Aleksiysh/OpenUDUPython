fout = open('out3.html','w',encoding='utf8')
print('''<html>
<body>
<table>''',file = fout)
for i in range(1,11):
    print('<tr>',file = fout)
    for j in range(1,11):
        print('<td><a href = \"http://'+str(i*j)+'.ru\">',i*j,'</a></td>',file = fout)
    print('</tr>',file = fout)
print('''       </table>
    </body>
</html> ''',file = fout)