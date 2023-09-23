import sys

input = sys.stdin.readline

'''
입력값
4 9
1 2 3 4 5
1 2 3 4 5
45678
45678
7
6
'''

# split() : 공백 사용하여 나누어 받음
# 4 9 입력 시 4와 9 사이 공백을 이용하여 n에 4, m에 9 입력

n, m = map(int, input().split())


# split() : 공백 사용하여 배열 만들기
# 1 2 3 4 5를 split()을 사용하여 배열로 생성

mapSplit1차배열 = list(map(int, input().split()))
mapSplit2차배열 = [list(map(int, input().split()))]

# rstrip() : 입력받는 모든 문자열을 분리하여 배열로 생성
# 45678을 rstrip()을 사용하여 배열로 생성 

mapRstrip1차배열 = list(map(int, input().rstrip()))
mapRstrip2차배열 = [list(map(int, input().rstrip()))]

# strip() : 앞 뒤 공백 제어
# 7 
# 6
# 입력 시 7과 6 뒤의 \n을 제거하고 출력

stripN = input().strip()
stripM = input().strip()

print('n, m : ', n, m)
print('mapSplit1차배열 : ', mapSplit1차배열)
print('mapSplit2차배열 : ', mapSplit2차배열)
print('mapRstrip1차배열 : ', mapRstrip1차배열)
print('mapRstrip2차배열 : ', mapRstrip2차배열)
print('stripN : ', stripN)
print('stripM : ', stripM)

