'''
■ 이진(분)탐색

1. 개념
  - 어떤 값을 찾을때 정렬의 특징을 이용해 빨리 찾음
  - 정렬되어 있을 경우, 어떤 값 찾을 때 : O(N) -> O(lgN)
  - 재귀 함수 사용
  - 처음부터 생각하기 어려움, 쉬운 방법부터 생각
    즉, 시간복잡도를 따져서 쉬운 방법이 어려울 시 선택
  - 예시
    - 1 ~ 4 숫자 중 특정 숫자를 찾아야 할 때
      - 모두 탐색 : O(N)
      - 이진 탐색 : O(lgN)
  - 핵심 코드(암기)
    def search(st, en, target):
    if st == en:
      # ~~
      return
    mid = (st + en) // 2 
    if nums[mid] < target:
      search(mid + 1, en, target)
    else:
      search(st, mid, target)
    
  - // 2의 의미는 2로 나눈 나머지는 버린다는 것. 즉, 5 / 2 == 2.5이므로 5 // 2 == 2임

2. 아이디어
  - 처음 아이디어
    - M개의 수마다 각각 어디에 있는지 찾기
    - for : M개의 수
    - for : N개의 수 안에 있는지 확인

  - 최종 아이디어
    - 투포인터 사용 ? => 투포인터는 연속해야 사용할 수 있으나, 해당 문제는 연속이 보장된 문제가 아니며, 
      어떤 값을 찾아내는 문제임 => 사용 불가
    - 이진탐색은 항상 정렬이 되어있어야 가능하므로 먼저 정렬을 해야함
      - N개의 수 먼저 정렬
      - M개의 수 하나씩 이진 탐색으로 확인
      
3. 시간복잡도
  - 처음 시간복잡도
    - for : M개의 수 > O(M)
    - for : N개의 수 안에 있는지 확인 > O(N)
    - O(MN) = 1e10 > 시간 초과
    - N : 10만, M : 10만이므로 최대 100억개가 됨
      => 초당 연산은 2억개 정도로 시간 초과 되므로 다른 방법을 찾아야 함

  - 최종 아이디어
    - N개의 수 정렬(암기) : O(N * lgN) : 10만 * (밑이 2인 log)log10^5
    - M개의 수 정렬(암기) : O(M * lgM) : 10만 * (밑이 2인 log)log10^5
    - O((N + M)lgN) : 10만 * (밑이 2인 log)log10^10 = 약 400만 = 2e5 * 20 = 4e6 => 가능

4. 기본 문제
  - 백준 1920 수 찾기
  - https://www.acmicpc.net/problem/1920

  - 문제
    N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
    
  - 입력
    첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
    다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
    모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

  - 출력
    M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

  - 예제 입력 
    5
    4 1 5 2 3
    5
    1 3 7 9 5

  - 예제 출력
    1
    1
    0
    0
    1
    
  - 변수
    - 탐색 대상 수 : int[]
      - 모든 수 범위 : -2^31 ~ 2^31 > INT 가능
    - 탐색 하려는 수 : int[]
      - 모든 수 범위 : -2^31 ~ 2^31 > INT 가능

  - 풀이 관련 최종 정리
    1. 아이디어
      - N개의 숫자를 정렬
      - M개를 for 돌면서 이진탐색
      - 이진탐색 안에서 마지막에 데이터를 찾으면 1 출력, 아니면 0 출력
      
    2. 시간복잡도
      - N개 입력값 정렬 = O(NlgN)
      - M개를 N개 중에서 탐색 = O(MlgN)
      - 총합 : O((N+M)lgN) > 가능
      
    3. 변수
      - N개 숫자 : int[]
      - M개 숫자 : int[]
        
6. TIP
  - 처음부터 생각하기 어려우므로 이중 for문을 사용하는 쉬운 방법부터 생각해야함
    - 어떤 값을 여러번 탐색해야 하는 경우
  - 입력의 개수가 1e5(10만) 정도의 개수라면 의심해봐야 함
'''

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort() # 이진탐색 하려면 정렬이 필수

def search(start, end, target):
  if start == end:
    if nums[start] == target:
      print(1)
    else:
      print(0)

    return
  
  mid = (start + end) // 2
  if nums[mid] < target:
    search(mid + 1, end, target)
  else:
    search(start, mid, target)

for each_target in target_list:
  search(0, N - 1, each_target)




