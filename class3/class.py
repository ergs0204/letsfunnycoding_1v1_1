# x=input("請輸入數字:")

# if not x.isdigit():
#     x=input("請重新輸入數字，不可以輸入其他的東西:")

# x=int(x)

x="123456789"

sum(map(int,x[::2]))
x[1::2]