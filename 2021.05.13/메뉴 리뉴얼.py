from itertools import combinations
def solution(orders, course):
    answer = []
    menus = dict()
    course_menu = []
    for i in orders:
        for j in course:
            for k in list(combinations(i,j)):
                menu = ''.join(sorted(k))
                if menu in menus.keys():
                    menus[menu] += 1
                else:
                    menus[menu] = 1
    menus = sorted(menus.items(),key = lambda x: x[1],reverse = True)
    max = 0
    for i in course:
        tmp = []
        for j in menus:
            if i == len(j[0]):
                tmp.append(j)
        course_menu.append(tmp)
    for i in course_menu:
        if len(i) != 0:
            max_num = i[0][1]
        else:
            break
        for j in i:
            if j[1] == max_num and j[1] != 1:
                answer.append(j[0])           
    return sorted(answer)
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
