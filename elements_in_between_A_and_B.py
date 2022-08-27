n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
co=0
for i in l:
    if i>=a and i<=b:
        co+=1
        print(i,end=' ')
if co==0:
    print("-1")