arr = ['l', 'k', 'p']
cnt = 0
for i in range(3):
    n = input()
    if n[0] in arr:
        try:
            arr.remove(n[0])
        except Exception as e:
            cnt = 0
        cnt += 1
    else: cnt = 0
if cnt == 3:
    print('GLOBAL')
else: print("PONIX")