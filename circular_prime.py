def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
def rev(n):
    reve=0
    while n:
        reve=reve*10+n%10
        n//=10
    return reve
n=int(input())
if prime(n):
    r=rev(n)
    if prime(r):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')
            