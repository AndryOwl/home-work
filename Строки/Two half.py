a = input()
v = a[len(a) // 2 + len(a) % 2:] + a[0:len(a) // 2 + len(a) % 2]
print(v)
