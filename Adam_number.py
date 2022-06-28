N=int(input())
sq=N**2
rev=0
while N:
    rev=rev*10+N%10
    N//=10
sqr=0
s=rev**2
while s:
    sqr=sqr*10+s%10
    s//=10
if sqr==sq:
    print('True')
else:
    print('False')