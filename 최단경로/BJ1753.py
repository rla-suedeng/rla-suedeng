import sys
import heapq

# 초기 설정
input = sys.stdin.readline
INF = sys.maxsize

#입력 받기
vertexs , edges = map(int, input().split())
start_v = int(input())

#가중치 리스트
dp = [INF]*(vertexs + 1)
heap = []
graph = [[] for _ in range(vertexs + 1)]

def Dijkstra(start):
    dp[start] = 0 # 시작 정점 가중치 초기화
    heapq.heappush(heap, (0, start))

    while heap:
        weight, curr = heapq.heappop(heap)
        if dp[curr] < weight:
            continue
        #w_node : 둘 사이 가중치 , next_node : 연결된 노드
        for w_node, next_node in graph[curr]:
            next_weight = w_node + weight
            if next_weight < dp[next_node]:
                dp[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))

for _ in range(edges):
    vertex_s, vertex_e, vertex_w = map(int, input().split())
    graph[vertex_s].append((vertex_w, vertex_e))

Dijkstra(start_v)
for i in range(1, vertexs + 1):
    print('INF' if dp[i] == INF else dp[i])