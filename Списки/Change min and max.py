a = [int(i) for i in input().split()]
mini = 0
maxi = 0
Min = a[0]
Max = a[0] 
for i in range(1, len(a)):
    if(a[i]) > Max:
        Max = a[i]
        maxi = i
    if(a[i] < Min):
        min = a[i]
        mini = i
change = a[mini]
a[mini] = a[maxi]
a[maxi] = change
for i in range(0, len(a)):
    print(a[i], end=" ")
