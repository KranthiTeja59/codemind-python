import math
n=int(input())
p=math.ceil(n**0.5)
q=math.sqrt(n)
if p==q:
    print("True")
else:
    print("False")