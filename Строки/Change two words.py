a = input()
b = a.find(" ")
print(a[b + 1:] + " " + a[0:b])
