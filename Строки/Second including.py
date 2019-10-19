a = input()
if a.count("f") >= 1:
    b = a.find("f")
    print(a.find("f", b + 1))
else:
    print(-2)
