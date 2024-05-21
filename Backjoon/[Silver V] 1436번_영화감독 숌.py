# 영화감독 숌
# SV_1436
import sys

# input
N = int(sys.stdin.readline())

num = 1
start = 667
while True:
    if N == 1:
        print('666')
        break

    if N > 1 and '666' not in str(start):
        start += 1
        continue
    
    num += 1
    if num == N:
        print(start)
        start += 1 
        break
    else:
        start += 1
        continue
