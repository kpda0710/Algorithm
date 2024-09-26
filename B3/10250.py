import sys
num = int(sys.stdin.readline().rstrip()) 
for i in range(num):
    count = 1
    h, w, n = map(int, sys.stdin.readline().rstrip().split(" "))
    while(1):
        if (h >= n):
            break
        n = n - h
        count += 1
    sys.stdout.write("{}\n".format(n * 100 + count))