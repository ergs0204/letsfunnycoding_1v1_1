# with open("test.py","r") as f: # f 是一個變數 file 的縮寫
#     x=f.read() # 讀整個檔案變一個字串

# with open("test.py","r") as f: 
#     x=f.read(10) 
#     print(x)
#     y=f.read(10) # 繼續往後讀
#     print(y)

# with open("test.py","r") as f:
#     x=f.readlines() # 一行一個字串 的 list
#     print(x)

# ["print('abc')\n", "print('123')\n", "print('657')"]

with open("test.py","r") as f:
    x=f.readline() # 只讀一行
    print(x)
# "print('abc')\n"