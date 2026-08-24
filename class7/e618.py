l=list(map(int,input().split()))
count={}

for number in l:
    if number in count: # 看有沒有這組對應
        count[number]+=1
    else:
        count[number]=1

for key,value in count.items(): 
    print(key,value)