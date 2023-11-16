n=5
st=n
sp=0
for a in range(n):
    for b in range(st):
        print('*',end=' ')
    for c in range(sp):
        print(' ',end=' ')
    print()
    st-=1
    sp+=1
