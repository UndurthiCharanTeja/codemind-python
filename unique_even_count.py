n=int(input())
l=list(map(int,input().split()))
b=set()
for i in l:
    if i%2==0:
        b.add(i)
print(len(b))        