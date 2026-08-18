x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x2=sum(x)
y2=sum(y)
a2=sum(a)
b2=sum(b)
print(f'{x2}:{y2}')
print(f'{a2}:{b2}')
if x2>y2 and a2>b2:
    print('Win')
elif x2<y2 and a2<b2:
    print('Lose')
else:
    print('Tie')