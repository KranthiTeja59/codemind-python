def is_prime(m):
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return False
    return True
m=int(input())
for j in range(m,m-10,-1):
    if is_prime(j):
        a=m-j
        np1=j
        break
for j in range(m,m+10):
    if is_prime(j):
        b=j-m
        np2=j
        break
if a<b:
    print(a)
else:
    print(b)