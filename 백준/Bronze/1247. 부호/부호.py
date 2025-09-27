s = []

for _ in range(3):
    n = int(input())
    number = [int(input()) for _ in range(n)]
    s.append(sum(number))

for i in range(3):
    if s[i] == 0:
        print(0)
    elif s[i] > 0:
        print('+')
    else:
        print('-')