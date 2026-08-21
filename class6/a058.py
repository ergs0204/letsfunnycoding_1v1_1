n=int(input())
y=[0,0,0] # [整除,餘1,餘2]
for i in range(n):
    x=int(input())%3 # 除3後剛好對應y裡面0,1,2的位子 就不需要那麼多if了
    y[x]+=1
print(y[0],y[1],y[2])