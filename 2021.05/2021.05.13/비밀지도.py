def solution(n, arr1, arr2):
    answer = []
    result = []
    formatting = '{0:0' + str(n) + 'd}'
    for i in range(len(arr1)):
        tmp = [' '] * n
        binary = formatting.format(int(bin(arr1[i])[2::]))
        print(binary)
        for j in range(0,len(binary)):
            if binary[j] == '1':
                tmp[j] = ('#')
        answer.append(tmp)
    for i in range(len(arr2)):
        tmp = answer[i]
        binary = formatting.format(int(bin(arr2[i])[2::]))
        for j in range(0,len(binary)):
            if binary[j] == '1':
                tmp[j] = '#'
        result.append(''.join(tmp))
    return result
print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
