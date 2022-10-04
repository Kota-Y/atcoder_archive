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
    n, m = i_map()
    x_list = i_list()

    NUM = 5050

    l = [0] * NUM
    for _ in range(m):
        c, y = i_map()
        l[c] = y

    dp = [[0] * NUM for i in range(NUM)]
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j-1] + x_list[i-1] + l[j]

        dp[i][0] = 0

        for j in range(i):
            dp[i][0] = max(dp[i][0], dp[i-1][j])

    ans = 0
    for i in range(n+1):
        ans = max(ans, dp[n][i])
    
    print(ans)

if __name__ == '__main__':
    main()
