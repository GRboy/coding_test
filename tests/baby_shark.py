from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
INF = int(1e9)
pos_x,pos_y = 0,0
shark_size = 2
n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int,input().split())))
for x in range(n):
    for y in range(n):
        if table[x][y] == 9:
            pos_x,pos_y = x,y
            table[x][y] = 0
def bfs(x,y):
    distance = [[INF]*n for _ in range(n)]
    visited= [[False]*n for _ in range(n)]
    visited[x][y] = True
    distance[x][y] = 0
    q = deque()
    q.append((x,y))
    while q:
        tmp_x,tmp_y = q.popleft()
        for i in range(4):
            nx,ny = tmp_x+dx[i],tmp_y+dy[i]
            if nx >= 0 and nx <n and ny >=0 and ny < n and table[nx][ny] <= shark_size and visited[nx][ny] == False:
                distance[nx][ny] = distance[tmp_x][tmp_y]+1
                visited[nx][ny] = 1
                q.append((nx,ny))
    return distance
def find_fish(dis):
    min = INF
    min_x,min_y = 0,0

    for x in range(n):
        for y in range(n):
            if dis[x][y] != INF and table[x][y] > 0 and shark_size > table[x][y]:
                if min > dis[x][y]:
                    min = dis[x][y]
                    min_x,min_y = x,y
    if min == INF:
        return False
    else:
        print(min,min_x,min_y)
        return min,min_x,min_y
answer = 0
ate = 0
while True:
    ret = find_fish(bfs(pos_x,pos_y))
    if ret == False:
        break
    else:
        table[ret[1]][ret[2]] = 0
        pos_x, pos_y = ret[1], ret[2]
        answer += ret[0]
        ate +=1
        if ate == shark_size:
            shark_size+=1
            ate = 0
print(answer)


