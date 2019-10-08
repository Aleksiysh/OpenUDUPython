s = input()
p1 = s.find("f")
p2 = s.rfind("f")
if p1 != -1:
    print(p1) if p1 == p2 else print(p1, p2)
