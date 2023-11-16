n=5
sp=n-1
st=1
for a in range(n):
    for b in range(sp):
        print(' ',end=' ')
    for c in range(st):
        print('*',end=' ')
    print()
    sp-=1
    st+=1
