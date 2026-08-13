x=input()
y=input()

# abc defg hi
# y= defg
# pos=3
# len(y)=4
# pos+3=6 => g

pos=x.index(y) # 找y在x裡面的位子
left=x[:pos] # 切其中一段 從頭到找到y的地方
right=x[pos+len(y):] # 從y後面開始切 len()=>長度
left=left[::-1]
right=right[::-1]
print(right+y+left)
