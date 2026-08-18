while True: # 永遠符合條件 會一直跑
    n=int(input())
    if n==0:
        break # 打破迴圈 停下來
    # 1到n 不要7的倍數
    for c in range(1,n):
        if c%7>0:
            print(c,end=" ")
    print()
    
