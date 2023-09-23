'''
LCS(Longest Common Subsequence) : 두 문자열 간 처음부터 순서대로 같은 문자열이 나오는 최대의 수
str1 : ACAYKP를 기준으로 CAPCAK와 동일한 문자는 최대 ACAK인 4가 나온다.
아래 그림으로 동적으로 표현하면 아래와 같음
ACAYKP 왼쪽의 0 열은 index를 1부터 시작하도록 하기 위함
  0 A C A Y K P
C 0 0 1 1 1 1 1
A 0 1 1 2 2 2 2
P 0 1 1 2 2 2 3
C 0 1 2 2 2 2 3
A 0 1 2 3 3 3 3
K 0 1 2 3 3 4 4
'''

import sys

input = sys.stdin.readline

str1 = str(input().strip())
str2 = str(input().strip())

print(str1)
print(str2)