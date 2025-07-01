t = int(input())
n = []
arr = []

arr.append([1,0])
arr.append([0,1])

for _ in range(t):
    n.append(int(input()))

for i in range(2, max(n) + 1):
    a = arr[i-1][0] + arr[i-2][0]
    b = arr[i-1][1] + arr[i-2][1]
    arr.append([a, b])

for j in n:
    print(arr[j][0], arr[j][1])