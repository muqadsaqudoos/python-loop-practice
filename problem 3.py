n=int(input('N:'))
a=n
for i in range(n):
    for j in range(i):
        print(end=' ')
    for j in range(a,0,-1):
        print('+',end='')
    a=a-1
    print()
a=n-1
for i in range(n-1):
    for j in range(a-1,0,-1):
        print(end=' ')
    for j in range(i+2):
        print('+',end='')
    a=a-1
    print()
        
