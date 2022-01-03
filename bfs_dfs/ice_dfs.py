n,m = map(int,input().split())
visited = [[0*m] for _ in range(n)]
board = list()
for _ in range(n):
    board.append(list(map(int,input())))

count = 0
def ice(x,y):

    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    if board[x][y] == 0:
        board[x][y] = 1
        ice(x+1,y)
        ice(x,y+1)
        ice(x-1,y)
        ice(x,y-1)
        return True
    else:
        return False


for x in range(n):
    for y in range(m):
        if ice(x,y) == True:
            count+=1
print(count)
