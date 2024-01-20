n=int(input())
l=list(map(int,input().split()))
ev=[]
od=[]
c=0
for i in range(0,n):
    if(l[i]%2==0):
        ev.append(i)
    else:
        od.append(i)
for i in range(1,len(od)):
    if((od[i]-od[i-1])==2):
        num=(od[i]-1)
        if num in ev:
            c=c+1
print(c)
        