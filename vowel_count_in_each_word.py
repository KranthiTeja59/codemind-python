n=input()
v="aeiouAEIOU"
n=n.split()
r=[]
c=0
for i in n:
    m=[]
    for j in i:
        if j in v:
            m.append(i)
    r.append(len(m))
print(*r)