x, y, w, h = map(int, input().split())

ans = [abs(w-x), abs(h-y), abs(x), abs(y)]
print(min(ans))
