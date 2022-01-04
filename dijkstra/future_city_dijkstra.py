import sys

input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
visited = [False]*(n+1)
distance = [INF]*(n+1)


graph = [[] for _ in range(n+1) ]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

end,middle = map(int,input().split())

def select_min_index():
    min = INF
    index = 0
    for i in range(1,n+1):
        if min >= distance[i] and visited[i] == False:
            min = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for node,dis in graph[start]:
        distance[node] = dis

    for _ in range(n-1):
        next = select_min_index()
        visited[next] = True
        for node,dis in graph[next]:
            if distance[node] > distance[next]+dis:
                distance[node] = distance[next]+dis

answer = 0
dijkstra(1)
answer += distance[middle]
visited = [0]*(n+1)
distance = [INF]*(n+1)
dijkstra(middle)
answer += distance[end]

if answer >= INF:
    print(-1)
else:
    print(answer)

