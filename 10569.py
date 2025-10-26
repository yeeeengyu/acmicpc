n = int(input())
temp = 0
for i in range(n):
    a, b = map(int, input().split())
    temp = (a - b) - 2
    if temp<0:
        print(-(temp))
    else:
        print(temp)