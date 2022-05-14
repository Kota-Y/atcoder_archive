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
    num_list = i_list()

    dp = [[0] * 2 for i in range(n)]

    dp[0][0] = INF
    dp[0][1] = num_list[0]
    dp[1][0] = num_list[0]
    dp[1][1] = min(dp[0][0]+num_list[1], dp[0][1]+num_list[1])

    for i in range(2, n):
        for bool in range(2):
            if bool == 0:
                dp[i][bool] = dp[i-1][1]
            else:
                dp[i][bool] = min(dp[i-1][0]+num_list[i], dp[i-1][1]+num_list[i], dp[i-2][1]+num_list[i])
    # print(dp)
    # print('=====')

    ans_min = min(dp[n-1][0], dp[n-1][1])

    dp = [[0] * 2 for i in range(n)]

    dp[0][0] = 0
    dp[0][1] = INF
    dp[1][0] = INF
    dp[1][1] = dp[0][0]+num_list[1]

    for i in range(2, n):
        for bool in range(2):
            if bool == 0:
                dp[i][bool] = dp[i-1][1]
            else:
                dp[i][bool] = min(dp[i-1][0]+num_list[i], dp[i-1][1]+num_list[i], dp[i-2][1]+num_list[i])
    # print(dp)

    ans_min = min(ans_min, dp[n-1][1])

    print(ans_min)

if __name__ == '__main__':
    main()
