while True:
    try:
        n,m=map(int,input().split( ))
        a=n**2+m**2
        b=n*(n+m)/2
        c=m**2/2
        d=n*(n-m)/2
        e=a-b-c-d
        print(int(e))
        
    except:
        break
