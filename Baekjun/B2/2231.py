import sys
num = int(sys.stdin.readline().strip())
if (num - (9 * len(str(num)))< 0):
    temp = 0
else: 
    temp = num - (9 * len(str(num)))
val = False
for i in range(temp, num):
    count = 0
    arr = list(str(i))
    for j in arr:
        count += int(j)
    if (num == i + count):
        sys.stdout.write(f"{i}\n")
        val = True
        break
if (val == False):
    sys.stdout.write("0\n")