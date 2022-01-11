from itertools import combinations
from collections import deque
import copy

dx = [1,0,-1,0]
dy = [0,1,0,-1]
n,m = map(int,input().split())

lab = list()
temp = list()
target = list()
wall = list()
virus = list()
for _ in range(n):
    lab.append(list(map(int,input().split())))
for x in range(n):
    for y in range(m):
        if lab[x][y] == 0:
            target.append((x,y))
        elif lab[x][y] == 2:
            virus.append((x,y))
wall = list(combinations(target,3))

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        nx,ny = q.popleft()
        for i in range(4):
            cx,cy = nx+dx[i],ny+dy[i]
            if cx >= 0 and cx < n and cy >= 0 and cy < m and temp[cx][cy] == 0:
                temp[cx][cy] = 2
                q.append((cx,cy))
def safe_count():
    count = 0
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 0:
                count+=1
    return count

max = 0
for i in wall:
    temp = copy.deepcopy(lab)
    temp[i[0][0]][i[0][1]] = 1
    temp[i[1][0]][i[1][1]] = 1
    temp[i[2][0]][i[2][1]] = 1
    for x,y in virus:
        bfs(x,y)
    temp_max = safe_count()
    if temp_max > max:
        max = temp_max

print(max)






