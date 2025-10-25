def factorial(param):
    if param > 1:
        return (param * factorial(param - 1))
    else:
        return 1
    
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(factorial(b) // (factorial(b-a) * factorial(a)))