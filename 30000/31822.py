COUNT = 0
n = input()
a = int(input())
for i in range(a):
    arr = input()
    print(arr[:5], n[:5])
    if arr.startswith(n[:5]):
        COUNT += 1
print(COUNT)