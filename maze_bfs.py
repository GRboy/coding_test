from collections import deque
n,m = map(int, input().split())
map_ = list()
visited = [[0]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for _ in range(n):
    map_.append(list(map(int,input())))
def bfs(x,y):
    visited[x][y] = 1
    queue = deque()
    queue.append((x,y))
    while queue:
        nx,ny = queue.popleft()
        for i in range(4):
            nextx = nx+dx[i]
            nexty = ny+dy[i]
            if nextx <=-1 or nextx >=n or nexty <=-1 or nexty >=m or map_[nextx][nexty] == 0 or visited[nextx][nexty] != 0:
                continue
            else:
                queue.append((nextx,nexty))
                visited[nextx][nexty] = visited[nx][ny]+1
bfs(0,0)
print(visited[n-1][m-1])