def sum(n):
    sum1=0
    
    for i in str(n):
        sum1+=int(i)
    if sum1>0 and sum1<10:
        print(sum1)
    else:
        sum(sum1)

n=int(input())
sum(n)