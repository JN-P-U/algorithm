'''
■ BFS

1. 개념
  - 그래프 탐색 : 어떤 것들이 연속해서 이어질 때, 모두 확인하는 방법
    - Graph : Vertex(어떤 것) + Edge(이어지는 선 - 간선)
    
  - 그래프 탐색 종료
    - BFS : Breadth First Search(너비 우선 탐색)
      - 그림에서 1 - 2 - 5 - 3 - 4 - 6 순서로 탐색
    - DFS : Depth First Search(깊이 우선 탐색)
      - 그림에서 1 - 2 - 3 - 4 - 6 - 5 순서로 탐색

2. 작동원리
  - 시작점에 연결된  Vertex 찾기
  - 찾은 Vertex를 Queue에 저장
  - Queue의 가장 먼저 것 뽑아서 반복

3. 시간복잡도
  - BFS : O(V + E)
  
4. 기본 문제
  - 백준 1926 그림
  - https://www.acmicpc.net/problem/1926
  
  - 문제
    어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
    단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
    가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
    그림의 넓이란 그림에 포함된 1의 개수이다.

  - 입력
    첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 
    두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. 
    (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

  - 출력
    첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 
    단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
  
  - 예제 입력
    6 5
    1 1 0 1 1
    0 1 1 0 0
    0 0 0 0 0
    1 0 1 1 1
    0 0 1 1 1
    0 0 1 1 1

  - 예제 출력
    4
    9
  
  - 변수
    - 검색할 그래프에 대한 자료구조
      - 그래프 전체 지도 : int[][]
    - 방문여부 확인할 자료구조(재방문 금지용)
      - 방문 : bool[][]
    - Queue : BFS 실행
  
  - 풀이 관련 최종 정리
    1. 아이디어
      - 2중 for => 그래프 값 1 && 방문 X
      - BFS 돌면서 그림 개수 +1, 최대값을 갱신

    2. 시간복잡도
      - BFS : O(V + E)
      - V : m * n == 500 * 500 == 250,000
      - E : V * 4 == 4 * 500 * 500 == 1,000,000 
      - V + E : 250,000 + 1,000,000 === 125만
      - 1초에 연산 2억개 가능
      - 그러므로 가능!

    3. 변수
      - 그래프 전체 지도 : int[][]
      - 방문 : bool[][]
      - Queue(BFS)
'''
from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

# 3번
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
  rs = 1
  q = deque()
  q.append((y, x))
  
  while q:
    ey, ex = q.pop()
    for k in range(4):
      ny = ey + dy[k]
      nx = ex + dx[k]
      if 0 <= ny < n and 0 <= nx < m:
        if map[ny][nx] == 1 and chk[ny][nx] == False:
          rs += 1
          chk[ny][nx] = True
          q.append((ny,nx))
  return rs

# 2번
cnt = 0
maxv = 0
for j in range(n):
  for i in range(m):
    if map[j][i] == 1 and chk[j][i] == False:
      chk[j][i] = True
      # 전체 그림 개수 + 1
      cnt += 1
      # BFS > 그림 크기를 구해주고
      maxv = max(maxv, bfs(j, i))
      # 최대값 갱신 

print(cnt)
print(maxv)