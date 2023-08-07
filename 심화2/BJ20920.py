import sys
input = sys.stdin.readline

words, length = map(int, input().rstrip().split())
dic_list = {}

for i in range(words):
    temp = input().rstrip()

    if(len(temp) < length):
        continue
    else:
        if(temp in dic_list):
            dic_list[temp] += 1
        else:
            dic_list[temp] = 1

final_dic = sorted(dic_list.items(),  key=lambda member: (-member[1], -len(member[0]), member[0]))

for j in final_dic:
    print(j[0])