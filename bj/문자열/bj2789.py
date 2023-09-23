'''
sorted(str) : 문자열 'str' 정렬
''.join(sorted(str)) : sorted(str) 의 결과는 char[]이므로 이를 다시 String 문자열로 정렬된 문자열로 변경 해주는 것

" ".join(str(input())).split() : 인풋으로 받은 문자열의 공백 " "을 가지고 배열을 만든 다음 이를 다시 공백을 제거한 하나의 문자열로 치환하는 것

for i in range(len(arr), 0, -1): : range의 끝에서부터 역순 반복문 실행
'''

import sys

input = sys.stdin.readline

chker = ''.join(sorted('CAMBRIDGE')) 

inStr = str(input())

inStr = " ".join(inStr).split()

arr = []


for i in range(len(chker)):
    for j in range(0, len(inStr)):
      if chker[i] == inStr[j]:
        arr.append(j)
arr.sort()
# print(arr)

for i in range(len(arr), 0, -1):
  #  print(arr[i - 1])
   del inStr[arr[i - 1]]
   
print(''.join(inStr))