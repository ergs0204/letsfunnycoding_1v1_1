a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if (a>=b>=c):
    print(c,b,a)
elif (a>=c>=b):
    print(b,c,a)
elif (b>=a>=c):
    print(c,a,b)
elif (b>=c>=a):
    print(a,c,b)
elif (c>=a>=b):
    print(b,a,c)
elif (c>=b>=a):
    print(a,b,c)

if (a*a+b*b<c*c or a*a+c*c<b*b or b*b+c*c<a*a) and a+b>c and a+c>b and b+c>a:
    print('Obtuse')
elif (a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a) and a+b>c and a+c>b and b+c>a :
    print('Right')
elif (a*a+b*b>c*c or a*a+c*c>b*b or b*b+c*c>a*a) and a+b>c and a+c>b and b+c>a :
    print('Acute')
else:
    print('No')
#老師，我很對不起，我後來忘記你跟我說可以一次弄比較多而且不用寫這麼長的方法
#所以我就用了我就得寫法，請老師下次再教一次，對不起