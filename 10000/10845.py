queue = []
for i in range(int(input())):
    arr = input().split()
    match arr[0]:
        case 'push':
            queue.append(int(arr[1]))
            print(queue[-1])
        case 'pop':
            if len(queue) == 0: 
                print(-1)
            else: print(queue.pop())
        case 'size':
            print(len(queue))
        case 'empty':
            print(1 if len(queue) == 0 else 0)
        case 'front':
            print(queue[-1] if len(queue) > 0 else -1)
        case 'back':
            print(queue[len(queue) - 1] if len(queue) > 0 else -1)
        