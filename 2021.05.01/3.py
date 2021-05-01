def solution(ads):
    answer = 0
    ad = []
    cost = []
    new_ad = []
    
    sum = 0
    for i in ads:
        ad.append(i[0])
        cost.append(i[1])
    tmp = ad[0] + 5
    for i in range(1,len(ad)):
        sum += ((tmp - ad[i]) * cost[i])
        print(tmp - ad[i])
        tmp += 5
    return sum
