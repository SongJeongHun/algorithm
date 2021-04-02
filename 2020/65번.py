def solution():
    a=[1,2,3,4]
    b=['a','b','c','d']
    c=[]
    result=[]
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
        result.append(c)
        c=[]
    print(result)
solution()
