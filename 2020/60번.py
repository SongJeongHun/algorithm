def solution(student):
    index=1
    student.sort()
    for i in student:
        print("번호:",index," 이름:"+i)
        index+=1
solution(['강은지','김유정','박현서','최성훈','홍유진','박지호','김채리','한지호'])
        
