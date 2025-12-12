n = int(input())
cnt = 0
for i in range(n):
    arr = list(map(int, input().split()))
    if arr[0] >= 1000 or arr[1] >= 1600 or arr[2] >= 1500 or arr[3] <= 30 and arr[3] != -1:
        cnt += 1
print(cnt)