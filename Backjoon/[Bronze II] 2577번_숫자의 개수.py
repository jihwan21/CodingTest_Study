# 숫자의 개수
# B2_2577
import sys

lst = [0] * 3
for i in range(3):
    lst[i] = int(sys.stdin.readline().strip())

mul_res = lst[0] * lst[1] * lst[2]

res = [0] * 10
for k in str(mul_res):
    res[int(k)] += 1

for i in res:
    print(i)
