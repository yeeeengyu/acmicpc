zero = 0
one = 0

def fib(n):
    global zero; global one
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    else:
        return fib(n -1 ) + fib(n - 2)

for i in range(int(input())):
    n = fib(int(input()))
    print(zero, one)
    zero, one = 0, 0