import sys
while(1):
    val = True
    num = list(sys.stdin.readline().strip())
    if (num[0] == "0"):
        break
    for i in range(len(num) // 2):
        if (num[i] != num[len(num) - 1 - i]):
            val = False
    if (val):
        sys.stdout.write("yes\n")
    else:
        sys.stdout.write("no\n")