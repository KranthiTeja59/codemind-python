n=int(input())
arr=list(map(int,input().split()))
x=int(input())
f=-1
l=-1
for i in range(0,n):
    if arr[i]==x and f==-1:
        f=i
    if arr[i]==x:
        l=i
print(f,l)