p, m, c = map(int, input().split())
n = int(input())
total = [0]
for i in range(1, p+1):
    total.append(abs((p+m) * (m+c) - n))
    if total[len(total) - 1] > n:
        break
for i in range(1, m+1):
    total.append(abs((p+m) * (m+c) - n))
    if total[len(total) - 1] > n:
        break
for i in range(1, c+1):
    total.append(abs((p+m) * (m+c) - n))
    if total[len(total) - 1] > n:
        break
print(total[len(total) - 2])