def solution(n, k, cmd):
    del_arr = []
    pointer = [i for i in range(n)]
    t = []
    answer = ['O'] * n
    for i in cmd:
        if i == "C":
            del_arr.append(pointer[k])
            t.append(k)
            del pointer[k]
            if k == n - 1:
                k -= 1
            n -= 1
        elif i == "Z":
            target = del_arr.pop()
            target_index = t.pop()
            pointer.insert(target_index,target)
            if target_index <= k:
                k += 1
            n += 1
        elif "D" in i:
            k += int(i.split()[1])
        elif "U" in i:
            k -= int(i.split()[1])
    for i in del_arr:
        answer[i] = "X"
    return ''.join(answer)
print(solution(15,5,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]),del_arr)
    
    
    
        
    
    
    
