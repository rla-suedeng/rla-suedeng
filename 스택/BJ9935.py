import sys

stack = []

given = sys.stdin.readline().rstrip()  # 문자열 입력
boom = sys.stdin.readline().rstrip()

boom_len = len(boom)

for i in given:
    stack.append(i) #문자열 스택 저장하는 과정
    if i == boom[-1] and ''.join(stack[-boom_len:]) == boom:
        del stack[-boom_len:]

ans = ''.join(stack)

if ans == '':
    print('FRULA')
else:
    print(ans)
