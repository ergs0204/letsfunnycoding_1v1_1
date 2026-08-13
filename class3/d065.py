hp,bp,jimi=map(int,input().split())

# if a<b>c
# if b>a and b>c (and b>d and b>e .....

# big+if 
big=hp
if bp>big:
    big=bp
if jimi>big:
    big=jimi
print(big)

# max
# print(max(hp,bp,jimi)) # max=>最大 min=>最小