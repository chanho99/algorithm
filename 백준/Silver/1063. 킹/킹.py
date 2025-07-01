king, stone, n = input().split()
n = int(n)
moves = []

for _ in range(n):
    moves.append(input())

# 이동 정의
move = {
    "R": (1,0),
    "L": (-1,0),
    "B": (0,-1),
    "T": (0,1),
    "RT": (1,1),
    "LT": (-1,1),
    "RB": (1,-1),
    "LB": (-1,-1)
}

# king, stone 좌표값 치환
king_x = ord(king[0]) - ord('A')
king_y = int(king[1]) - 1

stone_x = ord(stone[0]) - ord('A')
stone_y = int(stone[1]) - 1

for i in moves:
    dx, dy = move[i]

    # king 이동 시도
    moved_king_x = king_x + dx
    moved_king_y = king_y + dy

    # king이 체스판을 벗어났는지 여부 확인
    if any(val < 0 or val > 7 for val in [moved_king_x, moved_king_y]):
        continue

    # king이 stone의 좌표로 이동하려는지 확인
    if moved_king_x != stone_x or moved_king_y != stone_y:
        king_x = moved_king_x
        king_y = moved_king_y
        continue

    # king이 이동한 방향으로 stone도 같이 이동
    else:
        moved_stone_x = stone_x + dx
        moved_stone_y = stone_y + dy

    # stone이 체스판을 벗어났는지 여부 확인
    if any(val < 0 or val > 7 for val in [moved_stone_x, moved_stone_y]):
        continue

    else:
        king_x = moved_king_x
        king_y = moved_king_y
        stone_x = moved_stone_x
        stone_y = moved_stone_y

# 마지막 위치 출력
print(chr(king_x + ord('A')) + str(king_y + 1))
print(chr(stone_x + ord('A')) + str(stone_y + 1))