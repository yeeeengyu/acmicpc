a, b = map(int, input().split())
TOTAL = []
for i in range(a):
    n = input().strip()
    TOTAL.append(n[::-1])
for i in TOTAL:
    print(''.join(i))