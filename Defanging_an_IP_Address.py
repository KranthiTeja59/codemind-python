st=input()
l=len(st)
for i in range(0,l):
    if st[i]=='.':
        print("[.]",end="")
    else:
        print(st[i],end="")