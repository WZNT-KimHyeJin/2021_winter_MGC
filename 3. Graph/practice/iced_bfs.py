# 탐색 시작 노드를 큐에 삽입하고 방문처리한다.
# 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은
# 노드를 모두 큐에 삽입하고 방문 처리한다.
# 위의 과정을 수행할 수 없을 때까지 반복한다.

# 처음 BFS로 어떻게 접근해야 할지 감이 오질 않아서 구글 검색 찬스를 빌렸다.

from collections import deque

n,m = map(int,input("얼음 판의 크기를 입력하시오 : ").split())

#그래프 생성
graph =[]
for i in range(n):
    graph.append(list(map(int,input("그래프의 데이터를 입력하시오: "))))

#상하좌우 탐색
dx =[0,0,1,-1]
dy =[1,-1,0,0]

def bfs(x,y):

    q= deque()
    q.append((x,y)) # 현재 위치를 큐에 집어넣음

    # 아직 상황에 맞는 적절한 자료형을 생각해서 판단하는 것이 어렵다
    # 자료형에 대한 기본적인 지식은 가지고 있지만 이런 상황에서는 튜플 자료형을 쓰는 것이 훨씬 효율적이라고
    # 생각이 닿지 못한다. 문제를 많이 많이 접해봐야 할 것 같다.

# 이미 탐색한 곳은 탐색을 중단한다.
    if graph[x][y] == 1:
        return False

    #현재 위치를 기준으로 BFS 탐색
    while q:
        x,y = q.popleft()
        # 큐에 튜플 자료형이 저장 되어 있으므로 변수 두 개에 데이터를 받아올 수 있다.

        graph[x][y] =1 # 현재 위치 값을 0에서 1로 변경

        #상하좌우 탐색
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 얼음 틀 범위에서 벗어나지 않으면서 그 위치의 값이 0인
            # 경우에만 큐에 삽입

            if 0<= nx <n and 0 <= ny <m and graph[nx][ny] ==0:
                q.append((nx,ny))

    return True # 모두 탐색했을 경우 True 반환

cnt =0

for i in range(n):
    for j in range(m):
        if bfs(i,j) == True:
            cnt +=1

print(cnt)