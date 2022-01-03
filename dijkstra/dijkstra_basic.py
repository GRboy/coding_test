import sys
input = sys.stdin.readline

INF = int(1e9)
n,d = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
visited = [False]*(n+1)

for _ in range(d):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

#가장 distance가 작은 node index 반환
def choose_min_node():
    min = INF
    index = 0
    for i in range(1,n+1):
        if min > distance[i] and visited[i] == False:
            min = distance[i]
            index = i
    return index
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for node,dis in graph[start]:
        distance[node] = dis

    for _ in range(n):
        i = choose_min_node()
        visited[i] = True
        for x,y in graph[i]:
            cost = distance[i]+y
            if distance[x] > cost:
                distance[x] = cost
dijkstra(start)
for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])