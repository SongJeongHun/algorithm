n = int(input())
cost = 0
cards = list(map(int,input().split()))
cards.sort()
print(cards)
for i in range(len(cards)):
    print(i + 1,cards[i])
    cost += ((i + 1) * cards[i])
    if cost >= n:
        print(cost)
        break

    

