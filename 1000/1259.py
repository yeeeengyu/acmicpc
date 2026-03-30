while True:
    arr = input()
    if arr == '0': break
    revarr = arr[::-1]
    
    if arr == revarr:
        print("yes")
    else: print('no')