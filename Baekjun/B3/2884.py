import sys
h, m = map(int, sys.stdin.readline().rstrip().split(" "))
if (m >= 45):
    sys.stdout.write("{} {}".format(h, m - 45))
else:
    if (h == 0):
        h = 23
        sys.stdout.write("{} {}".format(h, m + 60 - 45))
    else:
        sys.stdout.write("{} {}".format(h - 1, m + 60 - 45))