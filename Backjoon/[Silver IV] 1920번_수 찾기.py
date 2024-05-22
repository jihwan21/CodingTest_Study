# 수 찾기
# S4_1920
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_set = set(A)

for i in B:
    if i in A_set:
        print('1')
    else:
        print('0')

# set()은 N의 시간 복잡도를 가짐
# for문 안에 set(A) 위치 시키면 M x N의 시간 복잡도
# for문 밖에 set(A) 변수 생성 시 시간 초과 문제 해결
