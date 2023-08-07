# 겹치는게 있는지 확인하고 싶으면 set 사용하기
chat_log_num = int(input())

chat_log = set() # 중복 삭제 자료형
cnt = 0

for _ in range(chat_log_num):
    user = input()

    if(user != 'ENTER'):
        if user not in chat_log:
            cnt += 1
            chat_log.add(user)
    elif(user == 'ENTER'):
        chat_log.clear()

print(cnt)