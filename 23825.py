a, b = map(int, input().split())
if a//2 != b//2:
    if a//2 < b//2:
        print(a//2)
    else: print(b//2)
else:
    print(a//2)