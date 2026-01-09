import sys
sys.setrecursionlimit(10**7)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

max_dist = 0
max_node = 0

def dfs(node, dist):
    global max_dist, max_node
    visited[node] = True

    if dist > max_dist:
        max_dist = dist
        max_node = node

    for next_node, d in graph[node]:
        if not visited[next_node]:
            dfs(next_node, dist + d)

visited = [False] * (n + 1)
dfs(1, 0)

visited = [False] * (n + 1)
max_dist = 0
dfs(max_node, 0)

print(max_dist)