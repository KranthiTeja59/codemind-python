n=input()
l=len(n)
for i in range(0,l):
    c=0
    for j in range(0,l):
        if n[j]==n[i]:
            c+=1
    if c==1:
        print(i)
        break
if c!=1:
    print('-1')