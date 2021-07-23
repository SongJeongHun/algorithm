import heapq
def solution(n,vertex):
    graph = {i:{} for i in range(1,n + 1)}
    for i in vertex:
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 1
    result = list(dijkstra(graph,1).values())
    maxValue = max(result)
    print(result.count(maxValue))
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
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
