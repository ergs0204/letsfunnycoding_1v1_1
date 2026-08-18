x=int(input()) 
y=list(map(int,input().split())) 
a=x//2

if x%2==1:
    an1=y[a]
else:
    an2=y[a-1]
    an3=y[a]
    an1=(an2+an3)//2
print(an1)