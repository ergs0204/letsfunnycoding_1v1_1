while True:
    try:
        n=int(input())
        list_number=list(map(int,input().split()))
        list_number.sort()
        print(*list_number)

        # 或是

        # list2=[] # 正常
        # while len(list2)<n:
        #     small=min(list_number)
        #     list_number.remove(small)
        #     list2.append(small)
        # print(*list2)
        
    except:
        break