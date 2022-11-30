n=int(input())
l=list(map(int,input().split()))
k=sum(l)
g=k//n
c=0
for i in l:
    if g==i:
        c+=1
if c>0:
    print("True")
else:
    print("False")
    