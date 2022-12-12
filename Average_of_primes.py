n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        d.append(j)
        
f= sum(d)/len(d) 
print("%.2f"%f)
        