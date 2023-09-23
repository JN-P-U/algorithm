'''
print 시 타입 지정
ord() : char 타입의 ascii 코드 연산
'''

import sys

input = sys.stdin.readline

str = str(input())

base = 0
if str[0] != 'F':
  base = 4 - (ord(str[0]) - ord('A'))

if str == 'F':
  base = 0

elif str[1] == '+':
  base += 0.3

elif str[1] == '-':
  base -= 0.3

print('%.1f' %base)