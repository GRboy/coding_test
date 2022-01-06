INF = int(1e9)
#입력
n,m,start = map(int,input().split())
distance = [INF]*(n+1)
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]

#입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def get_min_index():
    min = INF
    index = 0
    for i in range(n+1):
        if distance[i] < min and visited[i] == False:
            min = distance[i]
            index = i
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for x,y in graph[start]:
        distance[x] = y
    for _ in range(n-1):
        next = get_min_index()
        visited[next] = True
        for x,y in graph[next]:
            cost = distance[next]+y
            if cost < distance[x]:
                distance[x] = cost

dijkstra(start)
max = 0
count = 0
for value in distance:
    if value < INF:
        count +=1
        if max < value:
            max = value

print(count-1,max,end = "")
