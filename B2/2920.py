import sys
input = list(map(int, sys.stdin.readline().strip().split()))
a = [1, 2, 3, 4, 5, 6, 7, 8]
d = [8, 7, 6, 5, 4, 3, 2, 1]
if (input == a):
    sys.stdout.write("ascending")
elif (input == d):
    sys.stdout.write("descending")
else:
    sys.stdout.write("mixed")