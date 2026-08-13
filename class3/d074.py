# 5
# 42 39 41 43 30

n=int(input())
# input一行，用空格分開後，全部轉成數字，小心int不要括號
# map(功能,東西們) 
classes=list(map(int,input().split()))

# max(東西1,東西2,東西3)
# max(東西們)

print(max(classes))


