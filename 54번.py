def solution():
    num=list(map(int,input().split(' ')))
    result=0
    for i in num:
        result+=i
    sequence_sum=len(num)*(2*min(num)+(len(num)-1))/2
    if result==sequence_sum:
        return print("YES")
    else:
        return print("NO")
solution()
    
