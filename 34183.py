n, m, a, b = map(int, input().split())
chair = 0
for i in range(n):
    chair += 3
if chair < m: print(0)
else:
    price = a * (chair - m)

    print(price + b)