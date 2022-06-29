n=int(input())
arr=input()
co=0
c=0
for i in arr:
    if i=='1':
        c+=1
    if i=='0':
        if c>co:
            co=c
        c=0
if co<c:
    co=c
print(co)
        