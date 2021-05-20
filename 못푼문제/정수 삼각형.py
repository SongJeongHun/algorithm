result = 0
index = 0
for i in range(int(input())):
    num = list(map(int,input().split()))
    if len(num) == 1:
        result += num[0]
    else:
        max_num = max(num[index:index + 2])
        print(max_num)
        index = num.index(max_num)
        result += max_num        
print(result)
   
