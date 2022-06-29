arr=list(map(int,input().split()))
l=len(arr)
f=0
s=0
for i in range(0,l):
    if arr[i]>f:
        if f>s:
            s=f
        f=arr[i]
    elif( arr[i]>s and arr[i]<=f):
        s=arr[i]
print((s-1)*(f-1))