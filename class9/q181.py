green,red=map(int,input().split())
n=int(input())
l=list(map(int,input().split()))
total=0

for i in l:
    a=i%(green+red)
    if a>=green:
        total+=red-a+green
print(total)