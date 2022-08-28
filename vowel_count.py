n=input()
c=[]
for i in n:
    if i in "aeiouAEIOU":
        c.append(i)
if c==[]:
    print("0")
else:
    print(len(c))