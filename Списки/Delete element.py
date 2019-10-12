a = [int(i) for i in input().split()]
n = int(input())
for i in range(n + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
for i in range(0, len(a)):
    print(a[i], end = " ")
