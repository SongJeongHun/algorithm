import re
def solution(s):
    while not bool(re.match('(([a-zA-Z0-9])\\2{1,})',s)):
        s = re.sub('(([a-zA-Z0-9])\\2{1,})', '', s)
    if len(s) != 0:
        return 0
    else:
        return 1
print(solution('baabaa'))
