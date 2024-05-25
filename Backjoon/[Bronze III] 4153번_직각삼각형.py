# 직각삼각형
# B3_4153
import sys

res = []
while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    
    max_n = max(lst)
    lst.remove(max_n)
    if max_n**2 == (lst[0]**2 + lst[1]**2):
        res.append('right')
    else:
        res.append('wrong')

for i in res:
    print(i)
