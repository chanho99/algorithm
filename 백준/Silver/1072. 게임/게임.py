x, y = map(int, input().split())

z = y * 100 // x

if z >= 99:
    print("-1")
else:
    high = 10 ** 9
    low = 1

    while low <= high:
        middle = (high + low) // 2
        value = ((y+middle) * 100) // (x+middle)

        if value == z:
            low = middle + 1
        elif value > z:
            high = middle - 1
            result = middle
            
    print(result)