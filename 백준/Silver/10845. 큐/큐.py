from collections import deque

n = int(input())
command = [input().split() for _ in range(n)]
queue = deque()

for i in range(n):
    if command[i][0] == "push":
        x = command[i][1]
        queue.append(x)
    elif command[i][0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[i][0] == "size":
        print(len(queue))
    elif command[i][0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command[i][0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[i][0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)