# 입력 받기
chat_log_num = int(input())
chat_log = list(input() for _ in range(chat_log_num))

# ENTER 기준 분할
chat_combined = ' '.join(chat_log)
chat_log = chat_combined.split('ENTER ')
chat_log.pop(0)
cnt = 0

# 실제 카운트
for i in range(len(chat_log)):
    chat_log[i] = chat_log[i].strip().split(' ')
    for j in chat_log[i]:
        if(chat_log[i].count(j) > 1):
            while(j in chat_log[i]):
                chat_log[i].remove(j)
            chat_log[i].append(j)

for i in range(len(chat_log)):
    cnt += len(chat_log[i])

print(cnt)
