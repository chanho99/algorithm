n = int(input())
a = []

def a_666(num):
  return '666' in str(num)

count = 0
num = 666

while True:
  if a_666(num):
    count += 1
    if count == n:
      print(num)
      break
  num += 1