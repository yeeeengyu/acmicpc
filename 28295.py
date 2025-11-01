total = 0
for i in range(10):
    n = int(input())
    match n:
        case 1:
            total += 90
        case 2:
            total += 180
        case 3:
            total -= 90
total %= 360
if total == 0:
    print("N")
elif total == 90:
    print("E")
elif total == 180:
    print("S")
elif total == 270:
    print("W")