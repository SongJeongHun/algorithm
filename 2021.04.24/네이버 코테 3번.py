"""
1. 최댓값과 최솟값의 차이가 d 이하이면 리스트의 평균값을 리턴
2. 그렇지 않으면 최댓값 최솟값을 뺀 최댓값과 최솟값의 차이가 d 이하이면 리스트의 평균값을 리턴
3. 그렇지 않으면 임의로 k 개를 선택한후 최댓값과 최솟값의 차이가 d 이하이면 유효값 만약 유효값이 여러개가 잆다면 유효값중 평균값이 작은 것을 리턴
4. 그렇지 않으면 오름차순으로 정렬한 후, 가운데 값을 리턴, 만약 리스트가 짝수 개라면 작은 값을 리턴
"""
from itertools import permutations
def solution(prices,d,k):
    p = prices.copy()
    gap = max(p) - min(p)
    if gap <= d:
        return int(sum(p) / len(p))
    p.remove(max(p))
    p.remove(min(p))
    gap = max(p) - min(p)
    if gap <= d:
        return int(sum(p) / len(p))
    price_list = list(permutations(prices,k))
    prices_list = []
    for i in range(len(price_list)):
        gap = max(price_list[i]) - min(price_list[i])
        if gap <= d:
            prices_list.append(int(sum(price_list[i]) / len(price_list[i])))
    if len(prices_list) != 0:
        return min(prices_list)
    prices.sort()
    mid = int(len(prices) / 2)
    if len(prices) % 2 == 0:
        return prices[mid]
    else:
        return prices[mid + 1]
print(solution([2,4,5,2],3,2))
