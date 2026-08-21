## 要習慣用i當作index

```py 
x=[9,3,7,2,7,3,6,1]
for i in range(len(x)):
    print(x[i])

# 建議不要
number=0
for i in range(len(x)):
    print(x[number])
    number+=1
# 或
number=-1
for i in range(len(x)):
    number+=1
    print(x[number])
```


## while
條件符合就會一直跑(不知道要跑幾次)，記得條件的東西要變

```py
n = int(input())

i = 0
while i <= n:
    print(i)
    i += 1
```

### 用途
輸入直到0
```py
n = int(input())

while n != 0:
    print("你輸入了", n)
    n = int(input())
```

累加不知道多少次
```py
total = 0

n = int(input())

while n != 0:
    total += n
    n = int(input())

print(total)
```

強制輸入數字
```py
x = input("請輸入數字:")

while not guess.isdigit():
    x = input("錯誤，請輸入數字:")

x=int(x)
print(f"你輸入的數字是 {x}")
```

讀不知道幾行
```py
while True:
    try:
        n = int(input())
        print(n * 2)
    except EOFError:
        break
```