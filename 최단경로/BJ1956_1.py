#플로이드-워셜 
import sys

input = sys.stdin.readline
INF = int(sys.maxsize)

V, E = map(int, input().split())
graph = [[INF] * (V+1) for _ in range(V+1)] #인접 행랼 초기화

for _ in range(E): # 값 삽입
    x, y, w = map(int, input().split())
    graph[x][y] = w

#경유지 via, 출발지 start, 도착지 end

for via in range(1, V+1):
    for start in range(1, V+1):
        for end in range(1, V+1):
            if graph[start][via] + graph[via][end] < graph[start][end]:
                graph[start][end] = graph[start][via] + graph[via][end]

ans = INF

for i in range(1, V+1):
    ans = min(ans, graph[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)