r=int(input('Rows:'))
for i in range(r):
    for j in range(i+1):
        print('+',end='')
    print()
for i in range(r-1,0,-1):
    for j in range(i):
        print('+',end='')
    print()
