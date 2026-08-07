# print(type(1))
# print(type(1.2))
# print(type("123"))

## 字串

x="abcdefghijk"
# print(x[6]) # 從0開始
# print(x[2:6]) # cdef 取其中一段，不會碰到end
# print(x[0:5:2]) # ace [start,end,interval] 
# print(x[::2]) # acegik 開頭預設:最前面 結尾預設:最後面 間隔預設:1
# # cfi => 2 5 8
# print(x[2:10:3]) # [2:9:3][2:10:3][2:11:3]
# print(x[1:9:4]) # bf 沒有j 因為不會碰到第9個
# print(x[4:0:-1]) # edcb 間格-1會反過來 4,3,2,1
# print(x[6::-2]) # geca 6,4,2,0
# print(x[::-1]) # 整個反過來
# print(dir(str)) # dir 可以看有什麼功能 舉例像是之前的split
# print(x.index("cde"))
print(x.find("cde"))


## 條件

# if condition: #如果
#     do something
#     do another thing
# elif condition: # 否則如果
#     do something
# else: #否則
#     do something

# a=int(input())
# b=int(input())
# if a==b: # = 是把東西塞到變數， 要比較的時候用 == 
#     print("相同")
# else:
#     print("不同")

# score=int(input())

# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else: # else 不需要條件
#     print("F")


# x=int(input())

# if x%2==0:
#     print("是2的倍數")
# if x%3==0:
#     print("是3的倍數")