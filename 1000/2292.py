n = int(input())
nbox = 1
cnt = 1

while n > nbox:
    nbox += 6 * cnt
    cnt += 1
print(cnt)