'''
문자열 다루는 함수
ord() : 문자열을 ascii 코드로 변환
chr() : 문자를 ascii 코드로 변환
배열을 문자열로 : ' '.join(str(ts) for ts in charArr)
'''

import sys

input = sys.stdin.readline

s = str(input().strip())
charArr = []

for i in range(26):
  charArr.append(str(-1))

for i in range(len(s)):
  if charArr[ord(s[i]) - ord('a')] == str(-1):
    charArr[ord(s[i]) - ord('a')] = str(i)

# 배열을 문자열로 만들기 - 1
# result = ''
# for i in range(len(charArr)):
#   result += str(charArr[i])
#   if i < len(charArr) - 1:
#     result += ' '

# 배열을 문자열로 만들기 - 2
result = ' '.join(str(ts) for ts in charArr)

print(result)