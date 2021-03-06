
# 그래프 탐색 알고리즘
> 그래프 탐색에 사용되는 알고리즘

## BFS / DFS 
### DFS : 깊이 우선 탐색
#### -> 재귀함수 혹은 스택 자료구조를 이용한다
#### -> 무한루프를 방지하기 위해 어떤 노드를 방문했었는지에 대한 여부를 검사해야 한다
#### -> 경로의 특징을 저장할 필요가 있는 문제에 적합하다.
#### -> 사용시 유리한 경우)
>	- 모든 노드를 탐색해야 하는 경우 (dfs 구현 상대적 쉬움)
>	- 경로의 특징을 저장할  필요가 있는 문제
	- 그래프의 규모가 큰 문제
#### ->동작 과정
>	1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
>	2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면
>	   해당 노드를 스택에 넣고 방문 처리
>	   방문하지 않은 인접 노드가 없을 경우 스택에서 최상단 노드를 꺼낸다.
>	3. 위의 과정을 수행할 수 없을 때까지 반복



### BFS : 너비 우선 탐색
#### -> Queue 자료구조를 이용한다.
#### -> 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾는 문제에 사용한다.
#### -> 사용시 유리한 경우)
>	- 최단거리 문제
#### -> 동작과정
>	1. 탐색 시작 노드를 큐에 삽입하고 방문처리한다.
>	2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에
>	   삽입하고 방문 처리한다.
>	3. 위의 과정을 수행할 수 없을 때까지 반복한다.
