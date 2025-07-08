from collections import Counter

n = int(input())
nnum = list(map(int, input().split()))
m = int(input())
mnum = list(map(int, input().split()))

count = Counter(nnum)
result = [count[num] for num in mnum]

print(*result)