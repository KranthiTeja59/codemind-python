def power(n):
    a,b=0,1
    i=0
    while True:
        c=2**i
        a=b
        b=c
        if b>n:
            d1=b-n
            d2=n-a
            break
        i+=1
    if d1<d2:
        return d1
    else:
        return d2
n=int(input())
print(power(n))