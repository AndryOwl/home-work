s = input().split()
m = 0
for i in range(1, len(s)-1):
    if int(s[i-1]) < int(s[i]) and int(s[i]) > int(s[i+1]):
        m += 1
print(m)
