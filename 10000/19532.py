a, b, c, d, e, f = map(int , input().split())
end = bool()
x, y = 0, 0

for i in range(-999, 1000):
    x = i
    for j in range(-999, 1000):
        y = j
        if (a*x) + (b*y) == c and (d*x) + (e*y) == f: 
            print(x, y)
            end = True
            break
    if end:
        break