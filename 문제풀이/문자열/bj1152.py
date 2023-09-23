'''
str.input() :  문자열을 괄호 안의 구분자로 배열로 만드는 내장 함수
'''
import sys

input = sys.stdin.readline

strArr = input().split()

print(len(strArr))