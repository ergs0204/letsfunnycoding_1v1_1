a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

# 讓a小b中c大
if a>b:
    a,b = b,a # 交換
if b>c:
    b,c=c,b

if a>b:
    a,b=b,a

print(a,b,c)

if a+b<c:
    print("No")
elif (a*a+b*b<c*c):
    print('Obtuse')
elif (a*a+b*b==c*c):
    print('Right')
elif (a*a+b*b>c*c):
    print('Acute')