t = int(input())

def caldis(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

for _ in range(t):
    pos = []
    dis = []

    for _ in range(4):
        a, b = map(int, input().split())
        pos.append((a, b))
    
    for i in range(4):
        for j in range(i + 1, 4):
            dis.append(caldis(pos[i], pos[j]))

    dis.sort()

    if dis[0] == dis[1] == dis[2] == dis[3] and dis[4] == dis[5]:
        print(1)
    else:
        print(0)