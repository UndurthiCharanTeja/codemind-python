def fun(n):
   
    t=0
    
    for j in str(n):
        rem=0
        for k in range(1,int(j)+1):
            if int(j)%k==0:
                rem+=1
        if rem==2:
            t+=1
            
    if t==len(str(n)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    fun(n)
else:
    print("Not Mega Prime")
    
    