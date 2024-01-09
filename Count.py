t=int(input())
n=list(map(int,input().split()))
c=0
k=0
for i in n:
    if(i%2==0):
        c=c+1
    else:
        k=k+1
print(c,k)
