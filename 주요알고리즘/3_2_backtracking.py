'''
기본 문제 2
- 백준 15650 N과 M(2)
  - https://www.acmicpc.net/problem/15650
  - 문제
    - 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
      1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
      고른 수열은 오름차순이어야 한다.
    - 입력 : 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
    - 출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
            수열은 사전 순으로 증가하는 순서로 출력해야 한다.
    - 예제 입력 
        4 2
    - 예제 출력
        1 2
        1 3
        1 4
        2 3
        2 4
        3 4
  - 풀이 관련
    1. 아이디어
      - 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이 때, 방문여부 확인)
      - 재귀함수에서 M개를 선택할 경우, print
      
    2. 시간복잡도
      - N! > 10까지 가능하므로 8이라 가능

    3. 자료구조
      - 결과값 저장 int[]
      - 방문여부 체크 bool[]

'''
import sys

input = sys.stdin.readline

N,M = map(int, input().split())
rs = []
chk = [False] * (N + 1)

def recur(start, cnt):
  
  if cnt == M:
    print(' '.join(map(str, rs)))
    return
    
  for i in range(start, N + 1):
    if chk[i] == False:
      chk[i] = True
      rs.append(i)
      recur(i + 1, cnt + 1)
      chk[i] = False
      rs.pop()

recur(1, 0)