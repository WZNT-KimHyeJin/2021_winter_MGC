import sys

# 특정 원소가 속한 집합을 탐색
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합친다 == 간선 연결
def union(parent, a, b):
    rootA = find(parent,a)
    rootB = find(parent,b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

v,e = map(int, input("노드와 간선의 개수를 입력하시오 : ").split())
parent = [0]*(v+1) # ?????

edges =[]
result =0

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] =i

#모든 간선에 대한 정보 입력받기
for _ in range(e):
    a,b,cost =map(int,input("두 정점과 가중치를 입력하시오 :").split())
    edges.append((cost,a,b))
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정한다.

edges.sort()

for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 union한다.
    if find(parent,a) != find(parent,b):
        union(parent, a, b)
        result += cost

print("\nMST cost : ",result)


# <크루스칼 알고리즘>
# 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘.
# 크루스칼 알고리즘은 간선의 개수가 E개일때 O(ElogE)의 시간복잡도를 가진다
# 시간이 가장 오래 걸리는 부분이 간선 정렬 작업이며
# E개의 데이터를 정렬했을 떄의 시간복잡도는 O(ElogE)이기 때문이다.
# (파이썬에서 sort함수는 퀵정렬을 기본으로한다.== 퀵의 시간복잡도를 따라간다.)
# 크루스칼 내부에서 사용되는 서로소 집합 알고리즘의 시간 복잡도는 정렬 알고리즘의 시간 복잡도보다 작으므로 무시한다.