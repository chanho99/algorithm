n = int(input())
conference = []

for _ in range(n):
    a, b = map(int, input().split())
    conference.append((a, b))

conference.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for a, b in conference:
    if a >= end_time:
        count += 1
        end_time = b

print(count)