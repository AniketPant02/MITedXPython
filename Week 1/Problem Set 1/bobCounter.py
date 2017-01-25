bob = 0
for x in range(len(s)):
    if s[x:x+3] == "bob":
        bob += 1
print(str(bob))
