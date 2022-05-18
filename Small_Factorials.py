def fact(n):
    re=1
    for i in range(1,n+1):
        r=i%10
        re*=r
        i//=10
    return re
T=int(input())
for i in range(1,T+1):
    N=int(input())
    print(fact(N))