# 팰린드롬수
# B1_1259
import sys

while True:
    NUM = str(sys.stdin.readline().strip())
    if NUM == '0':
        break
    half = len(NUM) // 2

    if len(NUM) % 2 == 0: 
        if NUM[:half] == NUM[half:][::-1]:
            print('yes')
        else:
            print('no')
    else:
        if NUM[:half] == NUM[half+1:][::-1]:
            print('yes')
        else:
            print('no')
