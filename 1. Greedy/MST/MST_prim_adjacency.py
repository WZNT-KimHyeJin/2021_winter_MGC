# Prim 알고리즘
#   - 시작 정점에서 출발하여 정점을 하나씩 선택하며 신장트리 집합을 "확장"해나가는 방법
#   - 정점 선택 기반
# 1. 임의의 시작 정점을 하나 정한다. 시작 정점만 포함된 신장 트리 집합을 만든다.
# 2. N개의 정점이 모두 선택될 때 까지
#       - 신장트리의 집합에 포함된 정점에 인접했으며 아직 방문하지 않은 정점 중,
#         "최소 비용의 간선"이 존재하는 정점을 선택한다.
#       - 선택한 정점은 신장 트리 집합에 포함시킨다.


# 인접행렬을 이용한 Prim 알고리즘

from math import inf # 파이썬이 제공하는 가장 큰 수

def prim(start):
    global N, adj_mat
    visited_set = set() # 현재까지 방문한 정점들의 집합
    visited_set.add(start)
    distance =0

    # N-1개의 간선을 선택할 때 까지 반봇
    for _ in range(N-1):
        min_dist, next_node = inf, -1
        # min_dist : 현재 방문한 정점에서 갈 수 있는 간선의 최단거리
        # next_node : 현재 방문한 정점에서 최단 거리로 갈 수 있는 정점.

        for node in visited_set:
            # 현재까지 방문한 모든 정점에 대하여 탐색
            for j in range(0, N):
                if j not in visited_set and \
                        0 < adj_mat[node][j] < min_dist :
                    min_dist = adj_mat[node][j]
                    next_node=j
                    # 해당 정점과 연결 되어있고, 아직 방문하지 않은 모든 정점 중
                    # 소요 비용이 가장 작은 정점을 찾는다
        distance += min_dist
        visited_set.add(next_node)

    return distance


N, M = map(int, input("정점의 개수와 간선의 개수를 입력하시오:").split())
adj_mat = [[0]*N for _ in range(N)]

for _ in range(M):
    x,y,value = map(int,input("두 정점과 가중치를 입력하시오: ").split())
    # 정점 x와 y 사이의 가중치 == value
    adj_mat[x][y] = value
    adj_mat[y][x] = value

for i in adj_mat:
    print(i)
print("최단거리:",prim(1))

# Prim 알고리즘 시감 복잡도 : O(N^2)
# 정점에 비해 간선이 많은 밀집 그래프에서 적합한 알고리즘