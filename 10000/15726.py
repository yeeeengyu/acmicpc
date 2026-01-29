arr = list(map(int, input().split()))
print(int(arr[0] * arr[1] / arr[2]) if arr[0] * arr[1] / arr[2] > arr[0] / arr[1] * arr[2] else int(arr[0] / arr[1] * arr[2]))