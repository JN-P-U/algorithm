'''
■ MST(Minimum Spanning Tree)

1. 개념
  - Spanning Tree : 모든 노드가 연결된 트리
  - MST : 최소의 비용으로 모든 노드가 연결된 트리
  - 시간복잡도는 O(ElgE)
  - 즉, 어떻게 해야 최소 비용이 되는지를 찾는 것
  - MST는 간선이 양방향
  
  - MST 푸는 방법 : Kruskal or Prim
    - Kruskal : 전체 간선 중 작은 것부터 연결(Union-Find 알고리즘을 알아야 해서 어려움)
    - Prim : 현재 연결된 트리에 이어진 간선 중 가장 작은 것을 추가(heap 사용)

  - heap
    - 최대값, 최소값을 빠르게 계산하기 위한 자료구조
    - 이진 트리 구조
    - 처음에 저장할 때부터 최대값 or 최소값 결정하도록
    
  - 핵심코드
    heap = [[0, 1]]  # 시작점 : [비용, 노드번호]

    while heap:
      w, next_node = heapq.heappop(heap)
      if chk[next_node] == False:
        chk[next_node] = True
        rs += w
        for next_edge in edge[next_node]:
          if chk[next_edge[1]] == False:
            heapq.heappush(heap, next_edge)

2. 아이디어
  - 최소스패닝 트리 기본문제(외우기)
  - 간선을 인접 리스트 형태로 저장
  - 시작점부터 힙에 넣기
  - 힙이 빌 때까지
    - 해당 노드 방문 안한 곳일 경우
      방문 체크, 비용 추가, 연결된 간선을 새롭게 추가

3. 시간복잡도
  - Edge 리스트에 저장 : O(E)
  - Heap 안 모든 Edge에 연결된 간선 확인 : O(E + E)
  - 모든 간선 Heap에 삽입 : O(ElgE)
  - O(E + 2E + ElgE) = O(3E + ElgE) = O(E(3 + lgE)) = O(ElgE)
  
4. 기본 문제
  - 백준 1197 최소 스패닝 트리
  - https://www.acmicpc.net/problem/1197

  - 문제
    그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
    최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

  - 입력 
    첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
    다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
    이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 
    절댓값이 1,000,000을 넘지 않는다.
    그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 
    최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

  - 출력  
    첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
    
  - 예제 입력 1
    3 3
    1 2 1
    2 3 2
    1 3 3
      
  - 예제 출력 1
    3
  
  - 변수
    - Edge 저장 리스트 : (int, int)[]
      - 무게 최대 : 1e6 > INT 가능
      - 정점 번호 최대 : 1e4 > INT 가능
    - 정점 방문 : bool[]
    - MST 비용 : int(최대 2^31보다 이내)

  - 풀이 관련 정리
    1. 아이디어
      - MST 기본문제, 외우기
      - 간선을 인접리스트에 집어 넣기
      - Heap에 시작점 넣기
      - Heap이 빌 때까지 다음의 작업을 반복
        - Heap의 최소값을 꺼내서 해당 노드 방문 했는지 확인
        - 미방문 시 방문 표시
        - 해당 비용 추가
        - 연결된 간선들 Heap에 삽입
    
    2. 시간복잡도
      - MST : O(ElgE)

    3. 변수
      - 간선 저장 되는 인접리스트 : (무게, 노드번호)
      - 힙 : (무게, 노드번호)
      - 방문 여부 : bool[]
      - MST 결과값 : int

6. Tip
  - 최소 스패닝 트리 코드는 그냥 외우기
  - 중요한건 해당 문제가 MST 문제인지 알아내는 능력(유형 아래 두가지)
    - 모든 노드가 연결되도록 하는 것
    - 이미 연결된 노드를 최소의 비용으로 줄이기
'''

import heapq
import sys

input = sys.stdin.readline

V,E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
rs = 0

for i in range(E):
  a,b,c = map(int, input().split())
  edge[a].append([c,b])
  edge[b].append([c,a])

heap = [[0,1]] # [비용, 노드번호]

while heap:
  cost, each_node = heapq.heappop(heap)
  if chk[each_node] == False:
    chk[each_node] = True
    rs += cost
    for next_edge in edge[each_node]:
      if chk[next_edge[1]] == False:
        heapq.heappush(heap, next_edge)

print(rs)
