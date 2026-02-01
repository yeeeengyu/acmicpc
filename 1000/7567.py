arr = list(input())
total = 10
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        total += 5
    else:
        total += 10
print(total)