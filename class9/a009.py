# print(ord("1")) 49
# print(ord("*")) 42
# 輸入變成輸出 -7

# "a" => 97
# ord("a") order:編號 (編號幾號的符號)

# 97 => "a"
# chr(97) char:字母

s=input()
for i in s:
    print(chr(ord(i)-7),end="")