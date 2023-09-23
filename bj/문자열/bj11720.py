'''
sorted(str) : 문자열 'str' 정렬
'''

import sys

input = sys.stdin.readline

N = int(input())
strArr = sorted(str(input().strip()))

# print(N)
# print(strArr)

result = 0
for i in range(N):
    result += int(strArr[i])

print(result)