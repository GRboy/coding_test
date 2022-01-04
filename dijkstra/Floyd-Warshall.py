import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]
for x in range(1,n+1):
    for y in range(1,n+1):
        if x==y:
            graph[x][y] = 0
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b]= c

#k노드를 선택하여 a->b까지 가는 것과, a->k->b 중 작은 값을 최솟값으로 갱신
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print("INF");
        else:
            print(graph[i][j],end = " ")
    print()