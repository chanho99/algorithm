n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
order_t = 0
order_set_p = 0
order_each_p = 0

for i in range(6):
    order_t += (size[i] + t - 1) // t

order_set_p = n // p
order_each_p = n % p

print(order_t)
print(order_set_p, order_each_p)