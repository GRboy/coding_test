import heapq
testcase = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

INF = int(1e9)
def makeGraph(n,table):
    graph = [[] for _ in range((n * n) + 1)]
    index = 0
    for x in range(n):
        for y in range(n):
            index += 1
            for i in range(4):
                nx = x+dx[i]
                ny = y +dy[i]
                if nx >= 0 and nx < n and ny >=0 and ny < n:
                    graph[index].append((index+dg[i],table[nx][ny]))
    return graph
def dijkstra(start,n,graph):
    distance = [INF] * ((n * n) + 1)
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        d, next = heapq.heappop(q)
        if distance[next] < d:
            continue
        for i in graph[next]:
            cost = distance[next] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[n * n]
while testcase > 0:
    testcase -=1
    n = int(input())
    dg = [n,1,-n,-1]
    table = list()
    for _ in range(n):
        table.append(list(map(int,input().split())))

    graph = makeGraph(n,table)
    print(dijkstra(1,n,graph)+table[0][0])






