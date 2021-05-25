import re
def solution(files):
    file_dict = dict()
    heads = []
    head_dict = dict()
    result = []
    filea = sorted(files,key = lambda x:x.upper())
    for i in files:
        head,num = slicing(i)
        heads.append([head.lower(),num])
    for i in range(len(heads)):
        if heads[i][0] in head_dict.keys():
            head_dict[heads[i][0]].append(i)
        else:
            head_dict[heads[i][0]] = [i]
    print(heads,head_dict)
    for k,v in head_dict.items():
        if len(v) > 1:
            for j in range(len(v) - 1):
                one = v[j]
                two = v[j + 1]
                if int(heads[one][1]) > int(heads[two][1]):
                    result.append(sorted(v,key = lambda x:int(heads[x][1])))
    print(result)
    
    return files
def slicing(file):
    number = re.findall('\d+',file)
    index = file.index(number[0])
    head = file[:index]
    return head,number[0]

print(solution(	["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
