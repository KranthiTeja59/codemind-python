a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
l=set(x).intersection(y)
z=set(x).union(y)
print(len(z)-len(l))