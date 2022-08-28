n=input()
c=[]
d=[]
for i in n:
    if i in "aeiou":
        c.append(i)
    elif i in "AEIOU":
        d.append(i)
a=len(set(c))
b=len(set(d))
if a==5:
    print(True)
elif b==5:
    print(True)
else:
    print(False)
