n, b = map(int, input().split())
total = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in arr:
        total.append(j ** b % 1000)

for 