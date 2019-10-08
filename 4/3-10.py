s = input()
new = ""
for i in range(len(s)):
    if s[i] == "A":
        new += "B"
    elif s[i] == "B":
        new += "A"
    else:
        new += s[i]
print(new)
