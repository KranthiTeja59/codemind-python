n=int(input())
temp=n
m=n
x=0
while temp:
    r1=temp%10
    c=0
    while n:
        r2=n%10
        n//=10
        if r1==r2:
            c+=1
    if c>1:
        print('Not Unique Number')
        x=1
        break
    temp//=10
    if x==1:
        break
    n=m
if x==0:
    print('Unique Number')
    
    