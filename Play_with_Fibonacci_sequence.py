n=int(input())
f=0
s=1
ne=f+s
print(f,s,ne,end=' ')
while n-3:
    f=s
    s=ne
    ne=f+s
    print(ne,end=' ')
    n-=1