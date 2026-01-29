n = input()
match len(n):
    case 2: 
        print(int(n[0]) + int(n[1]))
    case 3:
        if n[2] == 0:
            print(int(n[0]) + int(n[1]))
        else: 
            print(int(n[0:2]) + int(n[2]))
    case 4:
        print(int(n[0:2]) + int(n[2:4]))