import sys
l = int(sys.stdin.readline().strip())
input = list(sys.stdin.readline().strip())
result = 0
count = 0
for i in input:
    result += (ord(i) - 96) * (31 ** count)
    count += 1
    result %= 1234567891
sys.stdout.write(f"{result}")