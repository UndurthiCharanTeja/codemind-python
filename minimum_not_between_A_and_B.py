n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
for i in l:
    if i>=a and i<=b:
        c.append(i)
    else:
        d.append(i)
if len(d)==0:
    print("-1")
else:
    print(min(d))