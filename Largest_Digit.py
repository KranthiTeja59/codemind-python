N=int(input())
h=0
while N!=0:
    r=N%10
    N//=10
    if r>h:
        h=r
print(h)
    