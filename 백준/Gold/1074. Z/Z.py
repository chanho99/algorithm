n, r, c = map(int, input().split())
size = 2**n
result = 0

while n >= 1:
    if r < size//2 and c < size//2:
        result += 0
    elif r < size//2 and c >= size//2:
        result += (size//2)**2
        c -= size // 2
    elif r >= size//2 and c < size//2:
        result += (size//2)**2*2
        r -= size // 2
    elif r >= size//2 and c >= size//2:
        result += (size//2)**2*3
        c -= size // 2
        r -= size // 2
    n -= 1
    size //= 2

print(result)