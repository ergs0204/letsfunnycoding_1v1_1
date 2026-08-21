n=int(input()) # 幾個數字
k=int(input()) # 除多少
y=[0]*k        # [整除,餘1,餘2....]
for i in range(n):
    x=int(input())%k 
    y[x]+=1

print(*y)