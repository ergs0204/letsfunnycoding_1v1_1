n=int(input())

for i in range(n):
    count={'0':0 , '1':0 , '2':0 , '3':0 , '4':0 , '5':0 , '6':0 , '7':0 , '8':0 , '9':0}
    b=int(input()) # 不需要a是字串版本
    for j in range(1,b+1): # j從1開始
        j2=str(j)
        # 不需要if 因為一位的話她就只會跑唯一一位
        # for k in range(len(j2)): # k跑的是順序
        #     count[j2[k]]+=1
        for k in j2: # k直接跑內容
            count[k]+=1
    print(*list(count.values()))

