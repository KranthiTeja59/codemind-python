N=int(input())
sum=0
a=list(map(int,input().split()))
for i in range(0,N):
    if a[i]%2==0:
        sum+=a[i]
print(sum)