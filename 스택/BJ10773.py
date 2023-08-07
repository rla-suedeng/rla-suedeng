import sys

num = int(sys.stdin.readline())
stack = []

for _ in range(num):
    money = int(sys.stdin.readline())
    if money == 0:
        stack.pop()
    else:
        stack.append(money)

if stack == []:
    print(0)
else:
    print(sum(stack))