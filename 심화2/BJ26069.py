meet = int(input())
dance = set()
tag = 0

for _ in range(meet):
    temp = input().split()
    if('ChongChong' in temp):
        dance.add(temp[0])
        dance.add(temp[1])
    elif('ChongChong' in dance):
        if(temp[0] in dance or temp[1] in dance):
            dance.add(temp[0])
            dance.add(temp[1])

print(len(dance))    

