from pathlib import Path

# 讀舊紀錄
path=Path("count.txt")
path.touch(exist_ok=True) # 如果檔案不存在就建立 第一次才有辦法讀 不然read 會壞掉

with open("count.txt","r") as f:
    s=f.read() # 先讀
x=int(s) if s else 0 #　如果有存過就用存的　沒有就用0
print(f"之前記錄到{x}")

# 玩遊戲 (enter +1)
while True:
    i=input("按enter+1 輸入-1結束")
    if len(i)!=0:
        break
    x+=1
    print(f"現在加到{x}")

# 結束前把紀錄存起來
print(f"結束在{x}，儲存中")
with open("count.txt","w") as f:
    f.write(str(x))