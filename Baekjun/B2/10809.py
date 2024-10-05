import sys
input = list(sys.stdin.readline().strip())
temp = [-1] * 26
for i, a in enumerate(input):
    if (temp[ord(a) - 97] == -1):
        temp[ord(a) - 97] = i
for i in temp:
    sys.stdout.write(f"{i} ")