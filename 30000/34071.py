a = int(input())
arr = []
for i in range(a):
    n = int(input())
    arr.append(n)
print('ez' if min(arr) == arr[0] else 'hard' if max(arr) == arr[0] else "?")