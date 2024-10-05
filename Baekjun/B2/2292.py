# 1 - 6 - 12 - 18
# 1 + 6 + 12 + 18
import sys
num = int(sys.stdin.readline().strip())
count = 1
room = 1
while(1):
    if (num <= count):
        sys.stdout.write(f"{room}")
        break

    count += 6 * room
    room += 1