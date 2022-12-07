n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
e=(len(l)//2)

for i in range(e):
    c.append(l[i])
for j in range(e,len(l)):
    d.append(l[j])

f=(sum(c))
h=(sum(d))
print(abs(f-h))
     