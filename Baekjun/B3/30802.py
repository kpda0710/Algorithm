import sys
n = int(sys.stdin.readline().strip())
size = list(map(int, sys.stdin.readline().strip().split()))
shirts, pens = map(int, sys.stdin.readline().strip().split())
s_count = 0
p_count = n // pens
for i in size:
    while(1):
        if (i > shirts):
            if (i % shirts == 0):
                s_count += i // shirts
            else:
                s_count += i // shirts + 1
            break
        elif(i == 0):
            break
        else:
            s_count += 1
            break    
sys.stdout.write(f"{s_count}\n")
sys.stdout.write(f"{p_count} {n - p_count * pens}\n")