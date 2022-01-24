import sys
import heapq
import collections


sys.setrecursionlimit(10**6)
# input = sys.stdin.readline()

n, m = map(int, input("노드와 간선의 개수를 입력하시오. : ").split())
graph = collections.defaultdict(list) # 빈 그래프 생성
visited = [0]*(n+1) # 노드의 방문 정보 초기화

# 무방향 그래프 생성
for i in range(m):
    u, v, weight = map(int, input("두 정점과 가중치를 입력하시오 : ").split())
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])

# 프림 알고리즘
def prim(graph, star_node):
    visited[star_node] =1 # 방문 갱신
    candidate = graph[star_node] # 현재 노드와 인접한 간선 추출
    heapq.heapify(candidate) # 우선순위 큐 생성
    mst =[]
    total_weight =0 # 전체 가중치

    while candidate:
        weight, u, v = heapq.heappop(candidate) # 가중치가 가장 적은 간선 추출

        if visited[v] ==0: #방문하지 않았을 경우
            visited[v]=1 # 방문 갱신
            mst.append((u,v))
            total_weight += weight

            for edge in graph[v]: # 다음 인접 간선
                if visited[edge[2]] == 0: # 방문한 노드가 아니라면 == 순환 방지
                    heapq.heappush(candidate, edge) # 우선순위 큐에 edge 삽입.

    return total_weight
print("\n최단 거리는 ",prim(graph,1))

# 시간 복잡도는 E logE