n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
h=len(a)//2
for i in range(len(a)):
    if i<h:
        s+=a[i]
print(s)
for i in range(h,n):
    s1+=a[i]
print(s1)
