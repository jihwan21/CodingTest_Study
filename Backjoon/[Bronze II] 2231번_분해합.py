# 분해합
# B2_2231
import sys

N = str(sys.stdin.readline().strip())

def sum_cal(N):
    res = 0
    for i in range(len(str(N))):
        res += int(str(N)[i])
    return res

lst = []
for i in range(int(N), 1, -1):
    sum = int(i) + sum_cal(i)
    if sum == int(N):
        lst.append(i)

if len(lst) == 0:
    print('0')
else:
    print(min(lst))
