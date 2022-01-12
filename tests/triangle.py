n = int(input())
tri = list()
for _ in range(n):
    tri.append(list(map(int,input().split())))

for i,sublist in enumerate(tri):
    if i ==0:
        continue
    for j,value in enumerate(sublist):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == len(sublist)-1:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1],tri[i-1][j])
def getMax():
    maximum = 0
    for i in range(n):
        if tri[n-1][i] > maximum:
            maximum = tri[n-1][i]
    print(maximum)
getMax()
