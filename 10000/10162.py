n = int(input())
five = 0
one = 0
ten = 0
if n % 10 != 0:
    print(-1)
else:
    while n != 0:
        if n % 300 == 0:
            n -= 300
            five += 1
        elif n % 60 == 0:
            n -= 60
            one += 1
        elif n % 10 == 0:
            n -= 10
            ten += 1
    print(five, one, ten)