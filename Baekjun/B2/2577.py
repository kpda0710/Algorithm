import sys
a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())
result = list(str(a * b * c))
for i in range(10):
    temp = result.count(f"{i}")
    sys.stdout.write(f"{temp}\n")