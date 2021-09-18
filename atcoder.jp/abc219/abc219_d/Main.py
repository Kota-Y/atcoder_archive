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
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n = i_input()
    x, y = i_map()
    num_list = i_row_list(n)

    dp = [[[INF] * (y+1) for _ in range(x+1)] for _ in range(n + 1)]

    dp[0][0][0] = 0

    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                dp[i + 1][j][k] = dp[i][max(0, j - num_list[i][0])][max(0, k - num_list[i][1])] + 1
                dp[i + 1][j][k] = min(dp[i][j][k], dp[i + 1][j][k])

    if dp[n][x][y] != INF:
        print(dp[n][x][y])
    else:
        print(-1)

if __name__ == '__main__':
    main()
