import sys
while (1):
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    numbers.sort()
    if (numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0):
        break
    elif (numbers[2] ** 2 == numbers[0] ** 2 + numbers[1] ** 2):
        sys.stdout.write("right\n")
    else:
        sys.stdout.write("wrong\n")