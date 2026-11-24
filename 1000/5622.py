dial = [    
    3, 3, 3, 
    4, 4, 4, 
    5, 5, 5, 
    6, 6, 6, 
    7, 7, 7, 
    8, 8, 8, 8, 
    9, 9, 9, 
    10, 10, 10, 10
]

n = list(input())
count = 0
for N in n:
    i = ord(N) - 65
    count += dial[i]
print(count)