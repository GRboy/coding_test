from collections import deque

n,m,k,x = map(int,input().split())
visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

count = 0
def bfs(start):
    visited[start] = 0
    q = deque()
    q.append(start)
    #visited를 어디에 추가해야하는지
    while q:
        next = q.popleft()
        for i in graph[next]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[next]+1

bfs(x)
for i in range(1,n+1):
    if visited[i] == k:
        count +=1
        print(i)
if count == 0:
    print(-1)



