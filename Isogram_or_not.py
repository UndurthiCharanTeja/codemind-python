s=input()
for i in s:
    c=s.count(i)
    if(c>1):
        print("False")
        break
if(c==1):
    print("True")
    