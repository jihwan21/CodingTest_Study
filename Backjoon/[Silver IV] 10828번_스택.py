# 스택
# S4_10828
import sys

N = int(sys.stdin.readline().strip())

stack = []
res = []
for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stack) == 0:
            res.append('-1')
        else:
            res.append(str(stack.pop()))
    elif order[0] == 'size':
        res.append(str(len(stack)))
    elif order[0] == 'empty':
        if len(stack) == 0:
            res.append('1')
        else:
            res.append('0')
    elif order[0] == 'top':
        if len(stack) == 0:
            res.append('-1')
        else:
            res.append(str(stack[-1]))

for i in res:
    print(i)
