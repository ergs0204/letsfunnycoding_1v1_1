# for number in range(1,6):
#     print(x+1)

# for i in range(6):
#     print(i)

# print(list(range(2,10,2)))
#  [開頭:結尾:間隔]
# int(input())

# name=input("請輸入名字")
# age=int(input("請輸入年紀"))

# print(f"名字: {name}，現在{age}歲，明天{age+1}歲")

# names=input().split()
# for name in names:
#     print(name)

## 累加
# x=10
# total=0
# for i in range(1,x+1):
#     total+=i
# print(total)

## 變更list
# x=[3,5,7,2,6]
# for i in range(len(x)):
#     x[i]*=2
#     x[i]+=2
# print(x)

## 找最大最小
x=[3,5,7,2,6]
small=x[0]
for i in x[1:]: # i 是裡面的數字
    if i<small:
        small=i

for i in range(1,len(x)): # i 是第"幾"個數字
    if x[i]<small:
        small=x[i]
print(small)
