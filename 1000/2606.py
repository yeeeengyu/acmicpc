_ = int(input())
n = int(input())
coms = [[0, 0] * n]
for i in range(n):
    a, b = map(int, input().split())
    coms[i].append(a, b)
print(coms[0][0])