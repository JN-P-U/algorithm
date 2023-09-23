'''
int(r) 문자형 숫자를 int로 변환
input().split() : 공백으로 배열
str(char) : char형을 문자열로 변환
'''
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
  r, s = input().split()
  result = ''
  for c in s:
    for j in range(int(r)):
      result += str(c)
  print(result)



