# 단어 공부
# B1_1157

word = str(input())

token = []
cnt = []
for t in word:
    t = t.upper()
    if t not in token:
        token.append(t)
        cnt.append(1)
    else:
        idx = token.index(t)    
        cnt[idx] += 1

cnt_sort = sorted(cnt)
if len(cnt_sort) > 1 and cnt_sort[-1] == cnt_sort[-2]:
    print("?")
else:
    idx = cnt.index(max(cnt)) # list에서 최대값 index return
    print(token[idx])
