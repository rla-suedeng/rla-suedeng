import sys
import heapq

#초기 설정
input = sys.stdin.readline
INF = 1e9

#전체 정점, 간선 이동
vertexs, edges = map(int, input().split())

graph = [[] for _ in range(vertexs + 1)] # 그래프표현 리스트

for _ in range(edges):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((cost, v2))
    graph[v2].append((cost, v1))

def Dijkstra(start): # 시작점이 start일 때 각 정점까지의 최단 거리
    dp = [INF]*(vertexs + 1) # 가중치 리스트
    heap = [] # 최소힙을 위한 리스트
    dp[start] = 0
    heapq.heappush(heap, (0, start)) # (가중치, 시작노드) 튜플로 대입

    while heap: # heap 리스트가 다 살펴볼때까지
        weight, curr = heapq.heappop(heap)
        
        if dp[curr] < weight :
            continue

        for w_node, next_node in graph[curr]:
            next_weight = w_node + weight
            if next_weight < dp[next_node]:
                dp[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))
        
    return dp # 최단 거리를 계산한 배열 자체를 넘기기

vertex1, vertex2 = map(int, input().split())

distance_1 = Dijkstra(1)
distance_v1 = Dijkstra(vertex1)
distance_v2 = Dijkstra(vertex2)

v1_path = distance_1[vertex1] + distance_v1[vertex2] + distance_v2[vertexs]
v2_path = distance_1[vertex2] + distance_v2[vertex1] + distance_v1[vertexs]

res = min(v1_path, v2_path)
print(res if res < INF else -1)




