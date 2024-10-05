import sys
num = list(map(int, sys.stdin.readline().strip().split()))
a = max(num)
b = min(num)
gcf = 0
lcm = 0
while(1):
    if (a != 0 and b != 0):
        temp = a - b * (a // b)
        a = b
        b = temp
    else:
        gcf = a
        break

lcm = num[0] * num[1] / gcf
sys.stdout.write(f"{gcf}\n{lcm:.0f}\n")