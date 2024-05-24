# 단어 정렬 12:41
# S5_1181
import sys

N = int(sys.stdin.readline().strip())
word = []
for _ in range(N):
    word.append(str(sys.stdin.readline().strip()))
word = list(set(word))

# 글자수 정렬
for idx, w in enumerate(word):
    min = w
    for i, k in enumerate(word[idx+1:]):
        if len(min) > len(k):
            min = k
            min_idx = i + (idx + 1)

    if len(min) < len(w):
        word[idx] = min
        word[min_idx] = w

# 알파벳 순서 정렬
for idx, w in enumerate(word):
    min = w
    for i, k in enumerate(word[idx+1:]):
        if len(min) != len(k):
            break
        else:
            if min > k:
                min = k 
                min_idx = i + (idx + 1)

    if w != min:
        word[idx] = min
        word[min_idx] = w

for i in word:
    print(i)
