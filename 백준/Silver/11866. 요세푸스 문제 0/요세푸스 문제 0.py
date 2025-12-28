n, k = map(int, input().split())
group = [i+1 for i in range(n)]
josephus = []
a = 0

while group:
    a = (a + k - 1) % len(group)
    josephus.append(group.pop(a))

print("<" + ", ".join(map(str, josephus)) + ">")