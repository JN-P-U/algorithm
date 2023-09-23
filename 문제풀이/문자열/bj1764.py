'''
map, split(), strip(), set
'''

import sys

input = sys.stdin.readline

n,m = map(int, input().split())

resultCnt = 0
result = []

s1 = set({})
s2 = set({})

for i in range(n):
  s1.add(input().strip())

for i in range(m):
  s2.add(input().strip())

s3 = s1.intersection(s2)

print(len(s3))

result = list(s3)
result.sort()

for s in result:
  print(s)