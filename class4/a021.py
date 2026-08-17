x,symbol,y=input().split()
x=int(x)
y=int(y)
if symbol=='+':
    z=x+y
    print(z)
elif symbol=='-':
    z=x-y
    print(z)
elif symbol=='*':
    z=x*y
    print(z)
elif symbol=='/':
    z=x//y
    print(z)