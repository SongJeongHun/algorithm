""" 1h52m """
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        index = -1
        prior = True
        exist = []
        for j in range(len(skill)):
            if not prior:
                break
            target = i.find(skill[j])
            exist.append(target)
            for k in range(len(exist) - 1):
                if exist[k] >= exist[k + 1] and exist[k + 1] >= 0:
                    prior = False
                    break
                else:
                    if exist[k] < 0 and exist[k + 1] >= 0:
                        prior = False
                        break
            if target == -1:
                exist[j] = -1
        if prior:
            answer += 1
    return answer
print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
