'''
str(input()) : input 문자열 받아서 처리
'''

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):

  strArr = str(input())

  result = 0
  partSum = 0
  # print(strArr[0])

  for j in range(len(strArr)):
    if strArr[j] == 'O':
      partSum += 1
      result += partSum
      # print('j : ', j, ' partSum : ', partSum, ' result : ', result)
    else:
      partSum = 0
  print(result)
        
