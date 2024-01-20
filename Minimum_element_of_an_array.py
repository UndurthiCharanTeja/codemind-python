n=int(input())
l=list(map(int,input().split()))
minn=l[0]
for i in range(1,n):
    if(l[i]<=minn):
        minn=l[i]
print(minn)
    
    