x,y=map(int,input().split())
s=0
for i in range(x):
    l=list(map(int,input().split()))
    for j in l:
        s+=j
print(s)