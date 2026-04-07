_ = int(input())
n = int(input())
coms = [[] for _ in range(n + 1)]
for i in range(n):
    a, b = map(int, input().split())
    coms[a].append(b)
    coms[b].append(a)


from collections import deque
visited = [False] * (n + 1)
queue = deque([1])
visited[1] = True
count = 0

while queue:
    node = queue.popleft()
    for i in coms[node]:
        if not visited[i]:
            visited[i] = True
            count += 1
            queue.append(i)
print(count)