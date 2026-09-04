a,b=list(map(int,input().split()))
a_clone=a
# 避免字串轉成數字再轉回字串
# 看b有沒有在a裡面
# True:有b, False:沒b
has_num=False
while a_clone>0:
    if a_clone%10==b: # 看個位數有沒有一樣
        has_num=True
    a_clone//=10 # 把a個位數刪掉 

if a%b==0 or has_num:
    print('YES')
else:
    print('NO')