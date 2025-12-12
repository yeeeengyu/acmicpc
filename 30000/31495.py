n = input()
arr = list(n)
end = ''
if arr.count('"') < 2:
    print("CE")
elif arr[0] != '"' or arr[len(arr) - 1] != '"':
    print("CE")
elif arr[0] == arr[1]:
    print("CE")
else:
    print(''.join(arr[1:len(arr) - 1]))
    