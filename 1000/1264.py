moeum = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
n = ''

while True:
    count = 0
    n = input()
    if n != '#':
        for i in moeum:
            count += n.count(i)
        print(count)
    else: break