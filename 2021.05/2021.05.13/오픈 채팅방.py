""" 37m"""
def solution(record):
    result = []
    nickDict = dict()
    commend = ''
    userID = ''
    nickname = ''
    for i in record:
        target = i.split(' ')
        if len(target) == 3:
            commend,userID,nickname = target
        else:
            commend,userID = target
        if commend == 'Enter':
            nickDict[userID] = nickname
            result.append(userID+"/님이 들어왔습니다.")
        elif commend == 'Leave':
            result.append(userID+"/님이 나갔습니다.")
        elif commend == 'Change':
            nickDict[userID] = nickname
    for i in range(len(result)):
        index = result[i].find('/')
        targetID = result[i][:index]
        result[i] = result[i].replace(targetID + '/',nickDict[targetID],1)
    return result
print(solution(["Enter uid42 L","Enter uid1234 Muzi","Leave uid42","Change uid42 MUzing", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
