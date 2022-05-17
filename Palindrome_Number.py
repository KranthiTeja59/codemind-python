T=int(input())
for i in range(1,T+1):
    m=int(input())
    rev=0
    temp=m
    while temp:
        r=temp%10
        rev=rev*10+r
        temp//=10
    if m==rev:
        print("True")
    else:
        print("False")
        