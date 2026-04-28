class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

n = int(input())
top = 0
stack = []

for i in range(n):
    arr = input().split()
    match arr[0]:
        case 'push':
            stack.append(int(arr[1]))
            top += 1
        case 'pop':
            if top > 0:
                print(stack[-1])
                stack.pop()
                top -= 1
            else: print(-1)

        case 'size':
            print(len(stack))
        case 'empty':
            print(1 if len(stack) == 0 else 0)
        case 'top':
            print(stack[-1] if len(stack) > 0 else -1)