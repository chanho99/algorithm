n = int(input())
age_name_index = []

for i in range(n):
  a, b = input().split()
  age_name_index.append((int(a), b, i))

sorted_list = sorted(age_name_index, key=lambda x: (x[0], x[2]))

for age, name, _ in sorted_list:
  print(age, name)