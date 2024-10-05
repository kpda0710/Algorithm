import sys
n = int(sys.stdin.readline().strip())
exam = list(map(int, sys.stdin.readline().strip().split()))
total = 0
max = max(exam)
for i in exam:
    total += i / max * 100
sys.stdout.write(f"{total / n}")