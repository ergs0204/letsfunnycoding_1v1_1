while True:
    try:
        n=int(input())
        count=0
        while n!=1:
            if n%2==0:
                n=n//2 # 維持是整數
            else:
                n=n*3+1
            count+=1
        print(count)
    except:
        break

# 33(11)  => 100(10) => 50(9) => 25(8) ......
# 200(11) => 100(10) => 50(x) => 25(x) ......

