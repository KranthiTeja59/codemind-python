n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(0,n):
        if i!=j and arr[i]==arr[j]:
            print(arr[i])
            c+=1
            break
    if c==1:
        break