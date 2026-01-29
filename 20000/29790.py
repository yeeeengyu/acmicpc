a, b, c = map(int, input().split())
print("Bad" if a < 1000 else "Good" if a>=1000 or b>=8000 or c>=260 else "Very Good" if a>=1000 and b>=8000 or c>=260 else '')