fibs = 0
fibbos = 0
def fib(n) :
    global fibs
    if n == 1 or n == 2:
        fibs += 1
        return 1
    else: return fib(n-1) + fib(n-2)

def fibbo(n):
    global fibbos
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        fibbos += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = int(input())
fib(n)
fibbo(n)

print(fibs % 1000000007, fibbos % 1000000007)