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

    ans_max = 0
    for i in range(n):
        for j in range(n):
            for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]):
                tmp_max = ''
                tmp_max += str_list[i][j]
                tmp_i, tmp_j = i, j
                for _ in range(n-1):
                    ni = tmp_i + dx
                    nj = tmp_j + dy
                    if ni < 0:
                        ni = n - 1
                    if ni >= n:
                        ni = 0
                    if nj < 0:
                        nj = n - 1
                    if nj >= n:
                        nj = 0
                    tmp_max += str(str_list[ni][nj])
                    tmp_i, tmp_j = ni, nj

                ans_max = max(ans_max, int(tmp_max))

    print(ans_max)

if __name__ == '__main__':
    main()
