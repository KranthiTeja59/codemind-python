N=int(input())
a=list(map(int,input().split()))
s=0
for i in range(1,N,2):
    s+=a[i]
print(s)