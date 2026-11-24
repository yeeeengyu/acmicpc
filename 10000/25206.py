scores = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

count = 0
gkrwja_count = 0
for i in range(20):
    n = input().split()
    if n[2] == 'P': continue

    gkrwja_count += float(n[1])
    count += scores[n[2]] * float(n[1])

print(f"{count / gkrwja_count:.6f}")