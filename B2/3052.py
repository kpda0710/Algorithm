import sys
numbers = list()
count = 0
for i in range(10):
    temp = int(sys.stdin.readline().strip())
    numbers.append(temp % 42)
set_numbers = set(numbers)
for i in set_numbers:
    count += 1
sys.stdout.write(f"{count}")