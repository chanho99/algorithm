n, m = map(int, input().split())
dogam = []
hashnum = {}
questions = []

for i in range(n):
    name = input()
    dogam.append(name)
    hashnum[name] = i + 1

for _ in range(m):
    q = input()
    questions.append(q)

for i in range(m):
    if questions[i].isdigit():
        print(dogam[int(questions[i]) - 1])
    else:
        print(hashnum[questions[i]])