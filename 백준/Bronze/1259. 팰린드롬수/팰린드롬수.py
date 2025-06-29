a = []

while True:
  input_data = input()
  if input_data == '0':
    break

  a.append(input_data)

for s in a:
  if s == s[::-1]:
    print('yes')
  else:
    print('no')