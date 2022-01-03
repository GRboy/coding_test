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

def dfs(graph, v):
    if visited[v] == 1:
        return
    visited[v] = 1
    print(v,end = ' ')
    for _ in graph[v]:
        dfs(graph,_)
dfs(graph,1)