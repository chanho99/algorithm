from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [-1] * (n + 1)
    queue = deque ([start])
    visited[start] = 0

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)

    return sum(visited[1:])

result = float('inf')
answer = 0

for i in range(1, n+1):
    kb = bfs(i)
    if kb < result:
        result = kb
        answer = i

print(answer)