n = int(input())
_ = input()
total = list(_)
for i in range(n - 1):
    arr = list(input())
    for i in range(len(total)):
        if _[i] != arr[i]:
            total[i] = '?'
print(''.join(total))