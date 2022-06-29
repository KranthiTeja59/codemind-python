n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(0,n):
    x=1
    while(x*x)<=arr[i]:
        if(x*x==arr[i]):
            sum+=arr[i]
        x+=1
print(sum)