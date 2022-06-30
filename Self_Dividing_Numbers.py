def sel(n):
    for d in str(n):
        if d=='0' or n%int(d)>0:
            return False
    return True
a=int(input())
b=int(input())
for n in range(a,b+1):
    if sel(n):
        print(n,end=' ')