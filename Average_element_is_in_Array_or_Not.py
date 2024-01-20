n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c=c+i
avg=c//n
if avg in l:
    print("True")
else:
    print("False")