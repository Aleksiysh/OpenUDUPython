n = int(input())
capitals = list()
for i in range(n):
    var = input()
    capitals.append(var)
capitals.sort()
for var in capitals:
    print(var)
