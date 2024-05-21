# 체스판 다시 칠하기
# S4_1018
import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(sys.stdin.readline().strip())

filter_cnt = []
def WB_filter(board, check, r, c):
    cnt = 0
    wb_gt = 'WBWBWBWB'
    bw_gt = 'BWBWBWBW'
    if check == 'W':
        for idx, row in enumerate(board[r:r+8]):
            if idx % 2 == 0:
                for gt, k in zip(wb_gt, row[c:c+8]):
                    if gt == k:
                        cnt += 1
            else:
                for gt, k in zip(bw_gt, row[c:c+8]):
                    if gt == k:
                        cnt += 1
    else:
        for idx, row in enumerate(board[r:r+8]):
            if idx % 2 == 0:
                for gt, k in zip(bw_gt, row[c:c+8]):
                    if gt == k:
                        cnt += 1
            else:
                for gt, k in zip(wb_gt, row[c:c+8]):
                    if gt == k:
                        cnt += 1

    result = min(cnt, 64 - cnt)                    
    return result

if N == 8 and M == 8:
    check = board[0][0]
    filter_cnt.append(WB_filter(board, check, 0, 0))
else:
    row_iter = N - 8 # 10 - 8 = 2
    col_iter = M - 8 # 13 - 8 = 5
    for r in range(0, row_iter+1):
        for c in range(0, col_iter+1):
                check = board[r][c:c+8][0]
                filter_cnt.append(WB_filter(board, check, r, c))

print(min(filter_cnt))
