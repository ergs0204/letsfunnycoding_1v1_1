d={}
x=0
while True:
    x=input()
    if x=="":
        break
    n,m=x.split()
    d[m]=n

while True:
    try:
        found=False
        a=input()
        if a in d: # 或用 d.keys()
            print(d[a])
        else:
            print('eh')
    except:
        break