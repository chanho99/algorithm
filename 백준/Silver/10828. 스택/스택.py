n = int(input())
command = [input().split() for _ in range(n)]
stack = []

for i in range(n):
    if command[i][0] == "push":
        x = command[i][1]
        stack.append(x)
    elif command[i][0] == "pop":
        if stack:
            x = stack.pop()
            print(x)
        else:
            print(-1)
    elif command[i][0] == "size":
        print(len(stack))
    elif command[i][0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command[i][0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)