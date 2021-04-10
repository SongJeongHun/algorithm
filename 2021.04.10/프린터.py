""" 47m """
def solution(priorities, location):
    count = 0
    pointer = location
    while(len(priorities) > 0):
        num_file = len(priorities) - 1
        max_file = max(priorities)
        while(priorities[0] != max_file):
            file = priorities.pop(0)
            if pointer == 0:
                pointer = num_file
            else:
                pointer -= 1
            for i in range(len(priorities)):
                if file < priorities[i]:
                    priorities.append(file)
                    break
        if pointer == 0:
            return count + 1
        priorities.pop(0)
        pointer -= 1
        count += 1
solution([2,1,3,2,2,5,7,5,4],2)
