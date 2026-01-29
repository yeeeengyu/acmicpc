n = int(input())
cnt = 0
arr = list(map(int, input().split()))
total = 0
for i in arr:
    if i == 1:
        cnt += 1
        total += cnt
    else:
        cnt -= 1
        total += cnt
print(total)