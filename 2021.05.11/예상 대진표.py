def solution(n,a,b):    
    return recursive([i for i in range(1,n + 1)],a,b,1)
def recursive(user,me,you,total_count):
    big = 0
    small = 0
    if me > you:
        big = me
        small = you
    else:
        big = you
        small = me
    if big - small == 1:
        if small % 2 == 1:
            return total_count
    new_user = []
    count = 1
    for i in user[::2]:
        if i + 1 == me or i == me:
            new_user.append(count)
            me = count
            count += 1
        elif i + 1 == you or i == you:
            new_user.append(count)
            you = count
            count += 1
        else:
            new_user.append(count)
            count += 1        
    return recursive(new_user,me,you,total_count + 1)
solution(8,4,5)
