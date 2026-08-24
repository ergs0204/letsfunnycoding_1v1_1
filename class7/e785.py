n=int(input())
d={}
for i in range(n):
    a=input() # 他喊的
    b=input() # 你喊的
    d[a]=b # 他喊的 對應到 你喊的

m=int(input())
for i in range(m):
    a=input() # 他喊的
    print(d[a]) # 把對應的內容print出來