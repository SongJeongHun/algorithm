def solution(answers):
    student = [0,0,0]
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    m1 = []
    m2 = []
    m3 = []
    for i in range(len(answers)):
        m1.append(s1[i % len(s1)])
        m2.append(s2[i % len(s2)])
        m3.append(s3[i % len(s3)])
    for i in range(len(answers)):
        if m1[i] == answers[i]:
            student[0] += 1
        if m2[i] == answers[i]:
            student[1] += 1
        if m3[i] == answers[i]:
            student[2] += 1
    max_count =  max(student)
    for i in range(len(student)):
        if max_count == student[i]:
            answer.append(i + 1)
    return answer
