import sys
num = int(input())

stack = []
ans = []
order = 1
possible = True

for _ in range(num):
    curr = int(input())
    while order <= curr :
        stack.append(order)
        ans.append('+')
        order += 1
    
    if stack[-1] == curr:
        stack.pop()
        ans.append('-')
    else:
        possible = False

if not possible :
    print('NO')
else:
    for j in ans:
        print(j)