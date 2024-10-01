import sys
n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
count = 0
for i in range(n):
    prime = True
    if (numbers[i] == 0 or numbers[i] == 1):
        continue
    else:
        for j in range(numbers[i] // 2 + 1):
            if (j == 0 or j == 1):
                continue
            else:
                if (numbers[i] % j == 0):
                    prime = False
                    break
    if (prime):
        count += 1

sys.stdout.write(f"{count}\n")
