import sys
num = int(sys.stdin.readline().strip())
for i in range(num):
    r, s = sys.stdin.readline().strip().split()
    temp = list(s)
    for j in temp:
        for k in range(int(r)):
            sys.stdout.write(f"{j}")
    sys.stdout.write("\n")