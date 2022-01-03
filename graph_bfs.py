from collections import deque
visited = [0]*9
graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    visited[start] =1
    while queue:
        x = queue.popleft()
        print(x,end = ' ')
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

bfs(graph,1)