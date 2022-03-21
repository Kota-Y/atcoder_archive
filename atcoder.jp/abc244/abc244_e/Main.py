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
MOD = 998244353

def main():
    n, m, k, s, t, x = i_map()

    edges = []
    for _ in range(m):
        u, v = i_map()
        edges.append((u-1, v-1))

    dp = [[[0] * 2 for _ in range(n + 1)] for _ in range(k + 1)]
    dp[0][s - 1][0] = 1
    
    for i in range(k):
        for u, v in edges:
            for bit in range(2):
                dp[i + 1][u][bit] += dp[i][v][bit ^ (v == x - 1)]
                dp[i + 1][v][bit] += dp[i][u][bit ^ (u == x - 1)]
                dp[i + 1][u][bit] %= MOD
                dp[i + 1][v][bit] %= MOD
    
    print(dp[-1][t - 1][0] % MOD)

if __name__ == '__main__':
    main()
