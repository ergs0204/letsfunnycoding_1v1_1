n=int(input())


for i in range(n):
    sen=input()
    d={}
    # 數小寫
    for j in sen:
        if j.isupper():
            j=j.lower()
        if j.islower():
            if j in d:
                d[j]=d[j]+1
            else:
                d[j]=1

    # 找最多的英文字母
    value=d.values()
    m=max(value)
    l=[]
    for a,b in d.items():
        if b==m:
            l.append(a)
    l.sort()
    print(*l,sep='')