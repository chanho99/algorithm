from collections import deque

com = int(input())
link = int(input())
arr = [[] for _ in range(com + 1)]

for _ in range(link):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (com + 1)

queue = deque([1])
visited[1] = True

while queue:
    current = queue.popleft()
    for neighbor in arr[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

print(visited.count(True) - 1)