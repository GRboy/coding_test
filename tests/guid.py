n = int(input())

member = list(map(int,input().split()))
member.sort(reverse=True)

index = 0
group = 0
while True:
    if index <= n-1 and index + member[index] <= n and member[index] > 1:
        group += 1
        index += member[index]
    else:
        break

print(group)