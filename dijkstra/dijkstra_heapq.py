import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
n,d = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF] *(n+1)

#그래프 생성
for _ in range(d):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

#이미 한번 heapq에서 빠진 node는 더 볼필요가 없다. 그게 그 노드의 최소값
def dijstra_heaq(start):
    h = []
    distance[start] = 0
    visited[start] = True
    heapq.heappush(h,(0,start))
    while h:
        dis,node = heapq.heappop(h)
        for x,y in graph[node]:
            cost = dis+y
            if cost < distance[x]:
                distance[x] = cost
                if visited[x] == False:
                    heapq.heappush(h,(distance[x],x))
                    visited[x] = True
dijstra_heaq(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
