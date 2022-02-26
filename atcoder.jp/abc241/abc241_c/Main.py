import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from array import array
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
def ceil(a, b): return (a + b - 1) // b
def floor(a, b): return a // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    n = i_input()
    str_list = s_row_list(n)

    # for i in range(n):
    #     print(*str_list[i])

    for i in range(n):
        for j in range(n):
            # 縦チェック
            tmp_count = 0
            flag = True
            for dx in range(6):
                if i + dx >= n:
                    flag = False
                    break
                if str_list[i+dx][j] == '#':
                    tmp_count += 1
            if tmp_count >= 4 and flag:
                print('Yes')
                exit()

            # 横チェック
            tmp_count = 0
            flag = True
            for dy in range(6):
                if j + dy >= n:
                    flag = False
                    break
                if str_list[i][j+dy] == '#':
                    tmp_count += 1
            if tmp_count >= 4 and flag:
                print('Yes')
                exit()

            # 斜めチェック1
            tmp_count = 0
            flag = True
            for dxy in range(6):
                if i + dxy >= n or j + dxy >= n:
                    flag = False
                    break
                if str_list[i+dxy][j+dxy] == '#':
                    tmp_count += 1
            if tmp_count >= 4 and flag:
                print('Yes')
                exit()

            # 斜めチェック2
            tmp_count = 0
            flag = True
            for dxy in range(6):
                if i - dxy < 0 or j + dxy >= n:
                    flag = False
                    break
                if str_list[i-dxy][j+dxy] == '#':
                    tmp_count += 1
            if tmp_count >= 4 and flag:
                print('Yes')
                exit()

    print('No')

if __name__ == '__main__':
    main()
