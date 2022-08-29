n=input()
c=999999999999
n=n.split(" ")
for j in n:
    co=0
    a=j
    for i in a:
        if i in "aeiou":
            co+=1
    if c>co:
        c=co
print(c)