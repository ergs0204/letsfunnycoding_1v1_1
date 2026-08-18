
```py
b=x[a:a+1:] # => b:其中一段
i=b[0]      # => i:拿出這段的唯一一個東西

i=x[a] # => 直接拿出這個東西
```

## print
```py
#sep => 會放在print的東西中間 預設空格
print(1,2,3,sep="--") # => 1--2--3
print(1,2,3,sep="x") # => 1x2x3

#end  => 會放在print結尾的東西 預設換行
print(1)
print(2)
# 1
# 2

print(1,end=" ")
print(2)
# 1 2
```