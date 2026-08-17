## 迴圈

for i in range()

讓 i 是 東西們:

```python
for i in range(5):
    print(i)
```

```python
x=["a","c","e"]
for i in x:
    print(i)
```

### range()
range(起點,終點,間隔) (和list一樣不會碰到終點)

range(5) => 0,1,2,3,4

range(2,6) => 2,3,4,5

range(2,10,2) => 2,4,6,8




### 常見作用
變更list

找最大

累加

## 其他
```py
x+=1 => x=x+1
y-=2 => y=y-2
z*=3 => z=z*3
a/=3 => a=a/3
a//=4 => a=a//4
```
fstring: f"{}" => 不需要轉換類別可以直接用大括號放變數進去
```py
name=input("請輸入名字")
age=int(input("請輸入年紀"))

print(f"名字: {name}，現在{age}歲，明天{age+1}歲")
```