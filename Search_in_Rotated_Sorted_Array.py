n=int(input())
arr=list(map(int,input().split()))
x=int(input())
p=-1
for i in range(0,n):
    if arr[i]==x:
        p=i
print(p)