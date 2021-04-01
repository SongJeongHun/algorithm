def solution(str):
    result={}
    for i in str:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    for i in result.keys():
        print(i,end='')
        print(result[i],end='')
solution(input())
        
