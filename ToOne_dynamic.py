from collections import deque

n = int(input())
queue = deque()
queue.append((n,0))
answer = 0
while queue:
    num,cnt = queue.popleft()
    if num == 1:
        answer = cnt
        break

    if num%5 == 0:
        queue.append((num/5,cnt+1))
    if num%3 == 0:
        queue.append((num/3,cnt+1))
    if num%2 == 0:
        queue.append((num/2,cnt+1))
    if num-1 >=1 :
        queue.append((num-1,cnt+1))
print(answer)