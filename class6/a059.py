from math import ceil # ceil=ceiling天花板 無條件進位，floor地板 無條件捨去

n=int(input())
for i in range(n): # 0,1,2,3,.....n-1
    number=0
    a=int(input())
    b=int(input())

    for c in range(ceil(a**0.5),int(b**0.5)+1): 
    # 注意b的部分要+1 例如 b=9 c應該要試到3 可是range(1,9**0.5) = range(1,3) 不會跑到三
        number+=c**2

    print(f'Case {i+1}: {number}') # Case後面的數字 用i+1 替代