n = int(input())
count = 0
if n%5!=0 and n%3!=0:
    count = -1

while True:
    print(count, n)
    if count == -1:
        break
    
    if n-5 >= 0:
        count += 1
        n -= 5
    elif n-3 >= 0:
        count += 1
        n -= 3
    
    if n-5<0 or n-3<0:
        break

if n == 3 or n == 5:
    print(count + 1)
else: print(count)