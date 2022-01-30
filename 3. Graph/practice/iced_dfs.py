# × M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은
# 1로 표시됩니다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어
# 있는 것으로 간주합니다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의
# 개수를 구하는 프로그램을 작성하세요. 다음의 4 × 5 얼음 틀 예시에서는 아이스크림이 총
# 3개 생성됩니다.

# DFS : 특정한 지점의 주변 상, 하, 좌, 우를 살펴 본 뒤에 주변 지점 중에서 값이 0 이면서 아직 방문하지 않은 지점이 있다면 해당 지점 방문
# 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 진행하는 과정을 반볻하면 연결된 모든 지점 방문 가능
# 모든 노드에 대하여 1~2번 과정 반복, 방문하지 않은 지점 카운트

def dfs(x,y):
    if x<=-1 or x >=n or y<=-1 or y>=m:
        return False
    if graph[x][y] ==0:
        graph[x][y]=1
        # 상하좌우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m = map(int, input("얼음틀의 크기를 입력하시오 : ").split())
#2차원 리스트의 맵 데이터 입력
graph=[]
for i in range(n):
    graph.append(list(map(int,(input("얼음틀의 모양을 입력하시오(구멍 : 0, 구멍x:1) : ")))))

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)

