from collections import deque

n, k = map(int, input().split())

def bfs(start, end):
    queue = deque([(start, 0)])
    visited = [False] * (100001)

    while queue:
        pos, count = queue.popleft()

        if pos == end:
            return count
        
        for next_pos in (pos-1, pos+1, pos*2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, count + 1))

print(bfs(n, k))