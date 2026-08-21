# n = int(input())
# while n != 0:
#     print("你輸入了", n)
#     n = int(input()) # 準備好n給下一次
# print("結束")

# while True: # True:符合 False:不符合
#     n=int(input())
#     if n==0:
#         break
#     print("你輸入了", n)
# print("結束")

# 題目不告訴你有幾行
while True:
    try:  # 試試看
        x=int(input())
        # if/elif/else... #
    except: # 如果試不了 try 裡面有問題就會跑到except
        break
