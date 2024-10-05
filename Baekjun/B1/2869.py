import sys
import math
a, b, v = map(int, sys.stdin.readline().strip().split())
day = math.ceil((v - a) / (a - b)) + 1
sys.stdout.write(f"{day}")
