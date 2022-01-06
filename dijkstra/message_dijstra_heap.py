import heapq

INF = int(1e9)
n,m,start = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))  #a에서 b까지 c거리
distance = [INF]*(n+1)

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dis,node = heapq.heappop(q)
        if distance[node] < dis:
            continue
        for n,d in graph[node]:
            cost = d + dis
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q,(distance[n],n))
dijkstra(start)
count = 0
max = 0
for i in distance:
    if i <INF:
        count +=1
        if max < i:
            max = i
print(count-1,max,end = " ")

