def (a,b,arr):
    for i in range(a,b+1):









n,q  = map(int,input().split())
arr = []


for i in range(n):
    arr.append(0)


for i in range(q):
    x, a, b = map(int,input().split())
    if (x == 0):
        zeroab(a,b,arr)
    elif(x == 1):
        oneab(a,b,arr)

There are N numbers a[0],a[1]..a[N - 1]. Initally all are 0. You have to perform two types of operations :

1) Increase the numbers between indices A and B by 1. This is represented by the command "0 A B"

2) Answer how many numbers between indices A and B are divisible by 3. This is represented by the command "1 A B".
        
































