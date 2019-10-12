a = [int(i) for i in input().split()]
p = int(input())
pos = 0
while pos < len(a) and a[pos] >= p:
    pos += 1
print(pos + 1)
