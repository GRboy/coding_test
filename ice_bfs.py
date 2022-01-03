from collections import deque

n,m = map(int , input().split())
visited = [[0]*m for _ in range(n)]

board = list()
for _ in range(n):
    board.append(list(map(int,input())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
count = 0

queue = deque()
for x in range(n):
    for y in range(m):
        if board[x][y] == 0 and visited[x][y] == 0:
            queue.append((x,y))
            visited[x][y] = 1
            count += 1
            while queue:
                tmp_x,tmp_y = queue.popleft()
                for i in range(4):
                    next_x = tmp_x + dx[i]
                    next_y = tmp_y + dy[i]
                    if next_x >=0 and next_y >=0  and next_x < n and next_y <m and visited[next_x][next_y] == 0 and board[next_x][next_y] == 0:
                        queue.append((next_x,next_y))
                        visited[next_x][next_y] = 1

print(count)