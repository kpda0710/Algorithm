import sys
n = int(sys.stdin.readline().rstrip())
temp = list(map(int, sys.stdin.readline().rstrip().split(" ")))
numbers = list()
for i in range(n):
    numbers.append(temp[i])
sys.stdout.write("{} {}".format(min(numbers), max(numbers)))