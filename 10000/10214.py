n = int(input())
for i in range(n):
    total = [0, 0]
    for i in range(9):
        a, b = map(int, input().split())
        total[0] += a
        total[1] += b
    print('Yonsei' if total[0] > total[1] else 'Korea' if total[0] < total[1] else 'Draw') 
