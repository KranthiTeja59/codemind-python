N=int(input())
s=0
temp=N
while temp:
    r=temp%10
    s+=r
    temp//=10
if N%s==0:
    print('True')
else:
    print('False')
    