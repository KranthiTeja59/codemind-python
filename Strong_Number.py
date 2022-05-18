def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
n=int(input())
s=0
temp=n
while temp:
    r=temp%10
    s+=fact(r)
    temp//=10
if s==n:
    print('The number',n,'is a strong number')
else:
    print('The number',n,'is not a strong number')
    
