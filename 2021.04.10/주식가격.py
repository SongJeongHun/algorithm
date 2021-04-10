""" 1h 03m """
def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        time = 0
        for j in range(i,len(prices) - 1):
            if prices[i] > prices[j]:
                break
            else:
                time += 1
        answer.append(time)  
    answer.append(0)
    return answer
solution([1,5,3,1,3])
