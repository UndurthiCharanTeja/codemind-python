n=int(input())
l=list(map(int,input().split()))

b=set()
for i in l:
    if i in l:
        
        
        b.add(i)
print(sum(b))        
        
        
       