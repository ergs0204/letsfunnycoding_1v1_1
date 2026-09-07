a,b,c=map(int,input().split())

det=b*b-4*a*c # determinant 判別式  b*b-4*a*c

if det<0: # 無解
    print("No real roots")
elif det==0: # 一個解
    x=-b/(2*a)
    print(f"One root x={x}")
else: # 兩個解
    x1=(-b+(det)**0.5)//(2*a) # // 就不需要int
    x2=(-b-(det)**0.5)/2//a
    x1,x2=max(x1,x2),min(x1,x2)
    # if x2>x1:
    #     temp=x1 # temperory 暫時的
    #     x1=x2
    #     x2=temp
    print(f"Two real roots x1={x1} , x2={x2}")