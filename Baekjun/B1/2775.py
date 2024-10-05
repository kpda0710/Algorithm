import sys
arr = {}
for i in range(1, 15):
    arr[(0, i)] = i
    arr[(i, 1)] = 1

def find(k, n):
    if (k, n) in arr:
        return arr[(k, n)]
    else:
        arr[(k, n)] = find(k, n - 1) + find(k - 1, n)
        return arr[(k, n)]

t = int(sys.stdin.readline().strip())
for i in range(t):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    sys.stdout.write(f"{find(k, n)}\n")
