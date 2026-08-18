x=input()
listn=[16,8,4,2,1]

nums=[]
for c in x: 
    nums.append(int(c))

numtotal=0

for i in range(5):
    number2=listn[i] # 16/8/4/2/1
    if nums[i]==1:
        numtotal+=number2 # 直接累積起來 不需要用list

print(numtotal)