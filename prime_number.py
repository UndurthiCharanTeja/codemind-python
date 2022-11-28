n=int(input())

cp=0
for i in range(1,n+1):
    if n%i==0:
        cp+=1
if cp==2:
    print("prime")
else:
    print("not a prime")
        