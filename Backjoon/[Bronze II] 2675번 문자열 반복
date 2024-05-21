# 문자열 반복
# B2_2675

test_num = int(input())
sent_lst = []
while True:
    sent = input().split(' ')
    sent_lst.append(sent)
    test_num -= 1

    if test_num == 0:
        break

for sent in sent_lst:
    num = int(sent[0])
    if len(sent) > 1:
        text = str(sent[1])

        result = ''
        for i in text:
            result += num * i
        print(result)
