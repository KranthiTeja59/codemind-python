def hcf(a,b):
    if a>b:
        a,b=b,a
    else:
        c=a
    while c>0:
        if a%c==0 and b%c==0:
            return c
        else:
            c-=1
N,M=map(int,input().split())
print(hcf(N,M))