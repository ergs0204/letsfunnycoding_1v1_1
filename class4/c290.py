list1=input()
A=list1[0::2]
AA=sum(A) # 後來在網路上查到sum()
B=list1[1::2]
BB=sum(B)
C=AA-BB
if C<0:
    C=-C
print(C)
