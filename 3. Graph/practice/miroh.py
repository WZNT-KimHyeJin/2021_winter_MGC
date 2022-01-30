# 동빈이는 N × M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이
# 있어 이를 피해 탈출해야 합니다.
# 동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩
# 이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어
# 있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 시작
# 칸과 마지막 칸을 모두 포함해서 계산합니다

from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))

    if graph[x][y] ==1:
        return False

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx>= n or ny <0 or ny >=m:
                continue
            if graph[nx][ny] ==0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                q.append((nx,ny))
    return graph[n-1][m-1]


n,m = map(int, input("미로의 크기를 입력하시오 :").split())

#상하좌우 탐색
dx =[0,0,1,-1]
dy =[1,-1,0,0]

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

print(bfs(0,0))

