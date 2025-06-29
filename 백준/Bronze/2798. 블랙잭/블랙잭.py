import itertools

n, m = map(int, input().split())
a = list(map(int, input().split()))

combs = list(itertools.combinations(a,3))

diff = float('inf')
for comb in combs:
  if m - sum(comb) >= 0:
    blackjack = m - sum(comb)
    if diff > blackjack:
      diff = blackjack

print(m - diff)