import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    checked[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n) and (nx, ny) in cabbage and not checked[nx][ny]:
            dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    cabbage = []
    group_count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        cabbage.append((x, y))

    # 탐색 확인 배열
    checked = [[False for _ in range(n)] for _ in range(m)]


    for a in range(m):
        for b in range(n):
            if (a, b) in cabbage and not checked[a][b]:
                dfs(a, b)
                group_count += 1

    print(group_count)