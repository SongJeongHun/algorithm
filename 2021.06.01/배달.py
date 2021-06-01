import heapq
def solution(N, road, K):
    answer = 0
    graph = {i:dict() for i in range(1,N + 1)}
    for i in road:
        if i[1] in graph[i[0]].keys():
            if graph[i[0]][i[1]] > i[2]:
                graph[i[0]][i[1]] = i[2]
                graph[i[1]][i[0]] = i[2]
        else:
            graph[i[0]][i[1]] = i[2]
            graph[i[1]][i[0]] = i[2]
    print(graph)
    graph = dijkstra(graph,1)
    for i in graph.values():
        if i <= K:
            answer += 1
    return answer
def dijkstra(graph,start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue,[distances[start],start])
    while queue:
        current_distance,current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent,weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue,[distance,adjacent])
    return distances
print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
