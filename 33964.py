# not solved
n = list(map(int, input().split())); m = list(map(int, input().split()))
cho = 72 - (n[0] * 13 + n[1] * 7 + n[2] * 5 + n[3] * 3 + n[4] * 3 + n[5] * 2)
han = 73.5 - (m[0] * 13 + m[1] * 7 + m[2] * 5 + m[3] * 3 + m[4] * 3 + m[5] * 2)

print(han, cho)
if han > cho:
    print('ekwoo')
elif han < cho:
    print('cocjr0208')