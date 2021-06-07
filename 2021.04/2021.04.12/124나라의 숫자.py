""" 1h1m """
def solution(n):
    global world_remain
    global world_quo
    world_remain = ['4','1','2']
    world_quo = ['1','2','4']
    return recursive(n,'')
def recursive(n,word):
    if n <= 3:
        word = world_quo[n - 1] + word
        return word
    else:
        quo = n // 3
        remain = n % 3
        word = world_remain[remain] + word
        if remain == 0 :
            quo -= 1
        return recursive(quo,word)
solution(18)
