def solution(n):
    return fibo(n) % 1234567
def fibo(num):
    cache = [0] * (num + 1)
    cache[0] = 0
    cache[1] = 1
    for i in range(2,num + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[num]
