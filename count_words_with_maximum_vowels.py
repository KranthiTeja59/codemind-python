n=input()
c=0
n=n.split()
c_=0
for j in n:
    co=0
    a=j
    for i in a:
        if i in "aeiou":
            co+=1
    if c<co:
        c=co
for j in n:
    co=0
    a=j
    for i in a:
        if i in "aeiou":
            co+=1
    if c==co:
        c_+=1
print(c_)