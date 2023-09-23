'''
sorted(str) : 문자열 'str' 정렬
'''

import sys

input = sys.stdin.readline

strArr1 = sorted(str(input()).strip())

strArr2 = sorted(str(input()).strip())

if strArr2 >= strArr1:
    print('go')
else:
    print('no')