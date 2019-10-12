a = [int(i) for i in input().split()]
count = 0
for i in range(len(a)):
    for j in range (0, len(a)-1):
        if a[j] == a[j+1]:
            count += 1
print(count)
