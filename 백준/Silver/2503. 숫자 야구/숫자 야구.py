from itertools import permutations

def absnumber(answer, guess):
    strike = sum(a == g for a, g in zip(answer, guess))
    ball = len(set(answer) & set(guess)) - strike
    return strike, ball
    
n = int(input())
question = []
cases = list(permutations(range(1, 10), 3))

for _ in range(n):
    number, strike, ball = input().split()
    each = [int(a) for a in number]
    question.append((each, int(strike), int(ball)))

for each, strike, ball in question:
    cases = [
        case for case in cases
        if absnumber(case, each) == (strike, ball)
    ]

print(len(cases))