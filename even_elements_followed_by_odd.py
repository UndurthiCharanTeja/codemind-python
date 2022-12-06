n=int(input())
a=list(map(int,input().split()))
b=[]
d=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        d.append(i)
print(*(b+d))        