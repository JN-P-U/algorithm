'''
■ 다익스트라

1. 개념
  - 다익스트라 : 한 노드에서 다른 모든 노드까지 가는데 드는 최소 비용
    - MST는 모든 노드를 잇는 최소 비용
  - 작동 원리
    - 간선 : 인접 리스트
    - 거리 배열 : 초기값 무한대로 설정, 힙 시작점 추가
    - 힙에서 현재 노드 뺴면서, 간선 통할 때 더 거리 짧아진다면 거리 갱신 및 힙에 추가
      
  - 핵심코드
    dist[K] = 0
    heapq.heappush(heap, (0, K))
    
    while heap:
      w, v = heapq.heappop(heap)
      if w != dist[v]:
        continue
      for nw, nv in edge[v]:
        if dist[nv] > dist[v] + nw:
          dist[nv] = dist[v] + nw
          heapq.heappush(heap, (dist[nv], nv))
      
2. 아이디어
  - 한 점에서 다른 모든 점으로의 최단 경로 > 다익스트라 사용
  - 모든 점 거리 초기값 무한대로 설정
  - 시작점 거리 0 설정 및 힙에 추가
  - 힙에서 하나씩 빼면서 수행할 것
    - 현재 거리가 새로운 간선 거칠때보다 크다면 갱신
    - 새로운 거리 힙에 추가

3. 시간복잡도
  - 다익스트라 시간복잡도 : ElgV
    - E : 3e5, lgV = 20
  - O(ElgV) = 6^6 > 가능
  - lg(10^6) ~= 20
    10^6 ~= 2^20
    10^3 ~= 2^10

4. 기본 문제
  - 백준 1753 
  - https://www.acmicpc.net/problem/1753

  - 문제
    방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
    단, 모든 간선의 가중치는 10 이하의 자연수이다.
    
  - 입력  
    첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 
    모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 
    셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
    이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
    서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
    
  - 출력 
    첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 
    시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
    
  - 예제 입력 1
    5 6
    1
    5 1 1
    1 2 2
    1 3 3
    2 3 4
    2 4 5
    3 4 6
    
  - 예제 출력 1
    0
    2
    3
    7
    INF

  - 변수
    - 다익스트라 사용 힙 : (비용(int), 다음 노드(int))[]
      - 비용 최대값 : 10 * 2e4 = 2e5 => INT 가능
      - 다음 노드 : 2e4 => INT 가능
    _ 거리 배열 : int[]
      - 거리 최대값 : 10 * 2e4 = 2e5 => INT 가능
    - 간선, 인접 리스트 : (비용(int), 다음 노드(int))[]
            
  - 풀이 관련 정리
    1. 아이디어
      - 한점 시작, 모든 거리 : 다익스트라
      - 간선, 인접리스트 저장
      - 거리배열 무한대 초기화
      - 시작점 : 거리배열 0, 힙에 넣어주기
      - 힙에서 빼면서 다음의 것들 수행
        - 최신값인지 먼저 확인
        - 간선을 타고 간 비용이 더 작으면 갱신
    
    2. 시간복잡도
      - 다익스트라 : O(ElgV)
        - E : 3e5
        - V : 2e4, lgV ~= 20
        - ElgV = 6e6 > 가능

    3. 변수
      - 힙 : (비용, 노드번호)
      - 거리 배열 : 비용 : int[]
      - 간선 저장, 인접리스트 : (비용, 노드번호)[]

6. Tip
  - 다익스트라 코드는 그냥 외우기!
  - 코드가 복잡하므로 연습 필요
  - 중요한건 해당 문제가 다익스트라 문제인지 알아내는 능력
    - 한 점에서 다른 점으로 가는 최소 비용
  
'''

import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int, input().split())
K = int(input())
edge = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
for i in range(E):
  u,v,w = map(int, input().split())
  edge[u].append([w,v])  

# 시작점 초기화

dist[K] = 0
heap = [[0, K]]

while heap:
  ew, ev = heapq.heappop(heap)
  if dist[ev] != ew: continue
  for nw, nv in edge[ev]:
    if dist[nv] > ew + nw:
      dist[nv] = ew + nw
      heapq.heappush(heap, [dist[nv], nv])


for i in range(1, V+1):
  if dist[i] == INF:
    print('INF')
  else:
    print(dist[i])
  

