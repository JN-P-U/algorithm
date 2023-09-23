"""
문제
N×M크기의 배열로 표현되는 미로가 있다.
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제
4 6
110110
110110
111111
111101

답 : 9
"""
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []

# graph = [list(map(int, input().rstrip())) for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

def bfs(y, x):
  dy = [-1, 1, 0, 0]
  dx = [0, 0, -1, 1]

  q = deque()
  q.append((y, x))
  
  while q:
    ey, ex = q.popleft()

    for k in range(4):
      ny = ey + dy[k]
      nx = ex + dx[k]

      if 0 <= ny < n and 0 <= nx < m:
        if graph[ny][nx] == 1:
          graph[ny][nx] = graph[ey][ex] + 1
          q.append((ny, nx))
  return graph[n - 1][m - 1]

print(bfs(0, 0))

