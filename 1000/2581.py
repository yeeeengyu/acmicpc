n = int(input())
m = int(input())

prime = []

for i in range(n, m+1):
    if i < 2: 
        continue

    isPrime = True
    for j in range(2, i):

        if i%j==0:
            isPrime = False
            break
    
    if isPrime: prime.append(i)

if prime:
    print(sum(prime))
    print(prime[0])
else: print(-1)
