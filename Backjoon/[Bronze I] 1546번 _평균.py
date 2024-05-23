# 평균
# B1_1546
import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

max_score = max(score)
sum = 0
for i in score:
    sum += i / max_score * 100

print(sum / N)
