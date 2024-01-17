n=int(input())
l=list(map(int,input().split()))
s=set(l)
k=[]
for i in s:
    if(l.count(i)==1):
        k.append(i)
if(len(k)==0):
    print(-1)
else:
    print(max(k))