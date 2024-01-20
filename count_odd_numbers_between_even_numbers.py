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
for i in range(1,len(ev)):
    if(ev[i]-ev[i-1]==2):
        num=ev[i]-1
        if num in od:
            c=c+1
print(c)