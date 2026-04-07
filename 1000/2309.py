arr = []
for i in range(9):
    n = int(input())
    arr.append(n)

a, b = 0, 0

for i in range(9):
    for j in range(i+1, 9):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            a, b = i, j
            break

total = []
for i in range(9):
    if i != a and i != b:
        total.append(arr[i])

for i in sorted(total):
    print(i)
