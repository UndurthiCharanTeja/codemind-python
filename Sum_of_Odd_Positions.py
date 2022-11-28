n=int(input())
l=list(map(int,input().split()))
sm=0
for j in range(n):
    if j%2!=0:
        sm=sm+l[j]
print(sm)
        
        
    
    
    