N=int(input())
a,b=0,1
print(a,b,end=' ')
for i in range(3,N+1):
    c=a+b
    print(c,end=' ')
    a,b=b,c
    c+=1
    
    