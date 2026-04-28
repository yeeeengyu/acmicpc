deck = [None] * 5
rear = 0
front = 0

def push_front(n):
    global front
    if isFull(): return -1
    else:
        front += 1
        deck.append(n)


def push_rear(n):
    if isFull(): return -1
    else:
        rear += 1
        deck.append(n)
        print(deck[rear])


def pop_front():

    global front
    if isEmpty(): return -1
    else:
        print(deck[front])
        deck.pop(front)

def pop_rear():
    if isEmpty(): return -1
    else:
        print(deck[rear-1])
        deck.pop(rear-1)

def isFull():
    global front
    if (rear + 1) % len(deck) == front:
        return 1
    else: return 0

def isEmpty():
    global front
    if rear == front: return 1
    else: return 0

for i in range(int(input())):
    print(deck)
    arr = input().split()
    match arr[0]:
        case 'push_front':
            push_front(arr[1])
        case 'push_rear':
            push_rear(arr[1])
        case 'pop_front':
            pop_front()
        case 'pop_rear':
            pop_rear()
        case 'size':
            print(len(deck))
        case 'empty':
            print(isEmpty())
        case 'front':
            print(deck[0] if isEmpty() == 0 else -1)
        case 'back':
            print(deck[-1] if isEmpty() == 0 else -1)
# rear front값 확인해봐야 할 듯