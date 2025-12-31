n, m = map(int, input().split())
knowtruenum, *knowtrue = map(int, input().split())

party = []
for _ in range(m):
    partynum, *num = map(int, input().split())
    party.append(num)

truth = set(knowtrue)
changed = True
while changed:
    changed = False
    for p in party:
        if truth & set(p):
            new_true = set(p) - truth
            if new_true:
                truth.update(new_true)
                changed = True

result = 0
for p in party:
    if not (truth & set(p)):
        result += 1

print(result)