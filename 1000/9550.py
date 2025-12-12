n = int(input())
total = 0
for i in range(n):
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    for j in arr:
        total += j // b
    print(total)
    total = 0