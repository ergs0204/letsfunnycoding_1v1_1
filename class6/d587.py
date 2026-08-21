n=int(input())
m=list(map(int,input().split()))
a=[0,0,0] # [1的數量,2的數量,3的數量]
for i in range(n):
    number=m[i]  # 數字: 1 or 2 or 3
    loc=number-1 # 位子: 0 or 1 or 2
    a[loc]+=1    # m[位子]+=1

print("1 "*a[0]+"2 "*a[1]+"3 "*a[2])