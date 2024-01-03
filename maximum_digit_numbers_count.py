def dig(k):
    c=0
    if k==0:
        return 1
    if k<0:
        k=abs(k)
    while k:
        k=k//10
        c=c+1
    return c
n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(0,n):
    k=dig(l[i])
    p.append(k)
for i in range(0,n):
    if(dig(l[i])==max(p)):
        print(l[i],end=" ")
    