n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

def check(x, y, size):
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                return False
            
    return True

def divide(x, y, size):
    if check(x, y, size) == True:
        if paper[x][y] == 1:
            return(0, 1)
        else:
            return(1, 0)

    new_size = size // 2
    w1, b1 = divide(x, y, new_size)
    w2, b2 = divide(x, y + new_size, new_size)
    w3, b3 = divide(x + new_size, y, new_size)
    w4, b4 = divide(x + new_size, y + new_size, new_size)

    return(w1+w2+w3+w4, b1+b2+b3+b4)

white, blue = divide(0, 0, n)
print(white)
print(blue)