str=input()
b={}
for i in str.split(" "):
    if i in b:
        b[i]+=1
    else:
        b[i]=1

print(max(b,key=lambda k:b[k]),"가 총",max(b.values()),"로 반장이 되었습니다")
