import heapq
def solution(n,vertex):
    answer = {}
    graph = {i:[] for i in range(1,n + 1)}
    for i in vertex:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    print(graph)
    print(bfs(graph,1))
    return answer
def bfs(graph,start):
    visited = []
    distance = 0
    need_visit = []
    need_visit.append([start,0])
    while need_visit:
        node,distance = need_visit.pop(0)
        if not node in visited:
            distance += 1
            visited.append(node)
            need_visit.extend(graph[node,distance])
    return visited 
solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
