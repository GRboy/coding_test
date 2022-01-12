from collections import deque
n,m = map(int,input().split())
linked = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
visit = [False]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
def bfs(start):
    visit[start] = True
    q = deque()
    q.append(start)
    while q:
        next = q.popleft()
        for node in graph[next]:
            if visit[node] == False:
                q.append(node)
                visit[node] = True
                linked[start].append(node)
                linked[node].append(start)

for i in range(1,n+1):
    visit = [False] * (n + 1)
    bfs(i)

answer = 0
for i in linked:
    if len(i) == n-1:
        answer += 1
print(answer)
