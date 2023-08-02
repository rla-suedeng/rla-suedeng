#BFS로 문제풀기
import sys
from collections import deque

MAX = 100001
N, K = map(int, sys.stdin.readline().split())

def BFS(start, end):
    visited = [-1 for _ in range(MAX)]
    visited[start] = 0
    queue = deque([start])

    while queue:
        check = queue.popleft()

        if check == end:
            return visited[check]
        
        if 0 <= check -1 < MAX and visited[check-1] == -1:
            visited[check-1] = visited[check] + 1 
            queue.append(check-1) 
                    
        if 0 < check * 2 < MAX and visited[check*2] == -1: 
            visited[check * 2] = visited[check] #이전 노드까지 걸린 시간 그대로
            queue.append(check*2)  # 순간이동시 0초 소모 == 우선순위

        if 0 <= check+1 < MAX and visited[check+1] == -1:
            visited[check+1] = visited[check] + 1
            queue.append(check + 1)

print(BFS(N, K))