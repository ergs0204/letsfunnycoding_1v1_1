n=int(input())
total=0
# n: 123 => 12 => 1 => 0
while n>0:
    total*=10   # 把數字x10 (往左移) 預留空間給個位數
    total+=n%10 # 個位數
    n//=10      # 把個位數削掉

print(total)