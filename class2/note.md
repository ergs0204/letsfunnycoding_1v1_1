type(x)
type() => 告訴我們類型(int,float,str etc)

多行註解 """ + """
"""
code 1
code 2
.....
"""

## 邏輯運算子
`<` `>` `>=` `<=` 
`==`(=是丟到變數裡，記得判斷用`==`) 
`!=`(不等於)
`in` (看有沒有在裡面 `"ab" in "abcde"` , `"ac" in "abcde"`)

條件一 and 條件二 => 且:兩個都要符合
條件一 or 條件二  => 或:其中一個符合就好
not 條件         => 不:反過來

買菜 and 買肉 and (買紅茶 or 買綠茶) and (not 買玩具)

## if elif else

```py
if condition: #如果
    do something
    do another thing
elif condition: # 否則如果
    do something
elif condition: # 否則如果
    do something
else: #否則
    do something
```
可以:
if 
if + else
if + elif
if + elif + else

只要一個 => 很多個elif 
每個都要 => 很多個if

## help 
看仔細說明

再terminal 中打 `python` 進入互動式介面
help(某個東西)  eg help(print) help(int) help("1") help(str.split)
看仔細說明，在說明中 enter 下一行， q 直接結束 help
exit() or Ctrl+z 結束互動式介面