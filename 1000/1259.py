while True:
    arr = input()
    match len(arr) % 2:
        case 0:
            a = arr[0: len(arr) / 2]
            b = arr[len(arr) / 2 : len(arr)]
            b = b[::-1]
            if a == b:
                print("yes")
            else: print('no')
        case 1:
            a = arr[0: len(arr) / 2]
            b = arr[len(arr) / 2 + 1:len(arr)]