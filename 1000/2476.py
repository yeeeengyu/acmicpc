n = int(input())
price = []
for i in range(n):
    arr = list(map(int, input().split()))
    setarr = set(arr)
    match len(setarr):
        case 1:
            price.append(10000 + (arr[0] * 1000))
        case 2:
            price.append(1000 + max(arr) * 100)
        case 3:
            price.append(max(arr) * 100)
print(max(price))