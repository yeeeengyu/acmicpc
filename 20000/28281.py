a, b = map(int, input().split())
arr = list(map(int, input().split()))

miniest = min(arr)
try:
    minies = arr[arr.index(min(arr)) + 1]
except IndexError as ie:
    minies = arr[arr.index(min(arr)) - 1]
print(miniest, minies)
print(miniest * b + minies * b)