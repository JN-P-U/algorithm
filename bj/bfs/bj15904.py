'''
count() : 배열에서 요수 갯수 찾는 함수
False 배열 : [False] * 배열 수
'''

import sys

input = sys.stdin.readline

str = str(input())

checker = [False] * 4

for i in range(len(str)):
  if str[i] == 'U':
    checker[0] = True
  elif str[i] == 'C' and checker.count(True) == 1:
    checker[1] = True
  elif str[i] == 'P' and checker.count(True) == 2:
    checker[2] = True
  elif str[i] == 'C' and checker.count(True) == 3:
    checker[3] = True

if checker.count(False) > 0:
  print('I hate UCPC')
else:
  print('I love UCPC')