timeList = ['12:30','13:20','14:13']
nowTime = '12:40'
answerList = []

def changeMin(time):
    return int(time.split(':')[0])*60+int(time.split(':')[1])
def changeHour(time):
    return '{:02d}시간 {:02d}'.format(time//60,time%60)

for i in timeList:
    if changeMin(i) - changeMin(nowTime) < 0:
        answerList.append("지났습니다.")
    else:
        anserList.append(changeHour(chageMin(i))-changeMin(nowTime))

print(answerList)
