n=int(input('N:'))
for i in range(1,n):
    asci=97
    for j in range(n+1):
        if(j==0):
            print(chr(asci),end='')
        else:
            asci=asci+i
            if(asci<=122):
                print(chr(asci),end='')
    print()
