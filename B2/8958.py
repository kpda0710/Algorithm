import sys
num = int(sys.stdin.readline().strip())
count = 0
score = 0
for i in range(num):
    ox = list(sys.stdin.readline().strip())
    for j in ox:
        if (j == "O"):
            score += 1 + count
            count += 1
        elif (j == "X"):
            count = 0
    sys.stdout.write(f"{score}\n")
    score = 0
    count = 0