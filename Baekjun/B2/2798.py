import sys
n, m = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
max = 0
for i in numbers:
    for j in range(numbers.index(i) + 1, n):
        for k in range(j + 1, n):
            if (max < i + numbers[j] + numbers[k] and m >= i + numbers[j] + numbers[k]):
                max = i + numbers[j] + numbers[k]
sys.stdout.write(f"{max}")