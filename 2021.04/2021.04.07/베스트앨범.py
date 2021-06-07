""" 1:29 """
def solution(genres, plays):
    an = []
    answer = []
    album = dict()
    for i in range(len(genres)):
        if album.get(genres[i]):
            album[genres[i]] += plays[i]
        else:
            album[genres[i]] = plays[i]
    key_album = dict(map(reversed,album.items()))
    for i in sorted(album.values(),reverse = True):
        tmp = []
        for j in range(len(genres)):
            if genres[j] == key_album[i]:
                tmp.append([j,plays[j]])
        answer.append(tmp)
    for i in answer:
        result = sorted(i,reverse = True,key = lambda x:x[1])
        max_num = len(result)
        if max_num < 2:
             an.append(result[0][0])
        else:
            for j in range(0,2):
                an.append(result[j][0])
    return ansolution(["classic", "pop", "classic", "classic"],[500, 600, 150, 800])
