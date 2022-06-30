def per(N):
    sum=0
    for i in range(1,N):
        if (N%i==0):
            sum+=i
    return sum
N=int(input())
if(N==per(N)):
    print('True')
else:
    print('False')
    