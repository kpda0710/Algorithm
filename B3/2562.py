import sys
numbers = []
max = 1

for i in range(9):
    input = int(sys.stdin.readline().rstrip())
    numbers.append(input)

for i in numbers:
    if (max < i):
        max = i
sys.stdout.write("{}\n".format(max))
sys.stdout.write("{}".format(numbers.index(max) + 1))