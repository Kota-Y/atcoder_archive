import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import ceil, floor, sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n = i_input()
    str_list = s_row_list(5)

    list0 = [['#', '#', '#'], ['#', '.', '#'], ['#', '.', '#'], ['#', '.', '#'], ['#', '#', '#']]
    list1 = [['.', '#', '.'], ['#', '#', '.'], ['.', '#', '.'], ['.', '#', '.'], ['#', '#', '#']]
    list2 = [['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#'], ['#', '.', '.'], ['#', '#', '#']]
    list3 = [['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#']]
    list4 = [['#', '.', '#'], ['#', '.', '#'], ['#', '#', '#'], ['.', '.', '#'], ['.', '.', '#']]
    list5 = [['#', '#', '#'], ['#', '.', '.'], ['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#']]
    list6 = [['#', '#', '#'], ['#', '.', '.'], ['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#']]
    list7 = [['#', '#', '#'], ['.', '.', '#'], ['.', '.', '#'], ['.', '.', '#'], ['.', '.', '#']]
    list8 = [['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#']]
    list9 = [['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#']]
    
    for i in range(n):
        tmp_list = [['.'] * 3 for _ in range(5)]
        for j in range(5):
            for k in range(3):
                if str_list[j][4*i+k+1] == '#':
                    tmp_list[j][k] = '#'
        if tmp_list == list0:
            print(0, end='')
        elif tmp_list == list1:
            print(1, end='')
        elif tmp_list == list2:
            print(2, end='')
        elif tmp_list == list3:
            print(3, end='')
        elif tmp_list == list4:
            print(4, end='')
        elif tmp_list == list5:
            print(5, end='')
        elif tmp_list == list6:
            print(6, end='')
        elif tmp_list == list7:
            print(7, end='')
        elif tmp_list == list8:
            print(8, end='')
        elif tmp_list == list9:
            print(9, end='')

    print()

if __name__ == '__main__':
    main()
