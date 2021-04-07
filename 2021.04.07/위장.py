"""1:56"""
def solution(clothes):
    closet = dict()
    count = 1
    for i in clothes:
        if closet.get(i[1]):
            closet[i[1]] += 1
        else:
            closet[i[1]] = 1
    for i in closet.values():
        count *= (i + 1)
    return count - 1
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])

