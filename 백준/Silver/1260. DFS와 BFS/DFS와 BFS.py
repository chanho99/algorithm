from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(node, visited):
    visited[node] = True
    print(node, end=' ')
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited)

def bfs(start):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

visited = [False] * (n+1)
dfs(v, visited)
print()
bfs(v)