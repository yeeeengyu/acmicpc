palinRes = 0
recurRes = 0

def recur(arr, a, b):
    global recurRes
    recurRes += 1
    if a >= b: return 1
    elif arr[a] != arr[b]: return 0
    else: return recur(arr, a+1, b-1)

def isPalin(arr):
    return recur(arr, 0, len(arr) - 1)

n = int(input())
for i in range(n):
    arr = input()
    print(isPalin(arr), recurRes)
    palinRes, recurRes = 0, 0