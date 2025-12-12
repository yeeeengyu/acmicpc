a = int(input()); b = int(input()); c = int(input()); d = int(input()); e = int(input())
time = 0

if a < 0:
    while a!=0:
        time += c
        a += 1

if a == 0:
    time += d

while a!=b:
    time += e
    a += 1
print(time)