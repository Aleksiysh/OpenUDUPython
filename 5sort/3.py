def keys(lst):
    return lst[1]


n = int(input())
capitals = list()
for i in range(n):
    var = list(input().split())
    capitals.append(var)

capitals.sort(key=keys)
for var in capitals:
    print(*var)
