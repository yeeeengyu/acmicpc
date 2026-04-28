head = None
cursor = head

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def move(self, n, cursor):
    match n:
        case "L":
            if self.prev is not None:
                cursor = self.prev
        case "D":
            if self.next is not None:
                cursor = self.next

import sys
input = sys.stdin.readline()

n = input()
n = list(n)

for i in range(int(input())):
    arr = input()
    arr = list(arr)

    match arr[0]:
        case 