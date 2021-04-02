data = []
for _ in range(int(input())):
    age,name = input().split()
    data.append([age,name])
data = sorted(data,key = lambda x: x[0])
for i,j in data:
    print(i,j,end = '\n')
