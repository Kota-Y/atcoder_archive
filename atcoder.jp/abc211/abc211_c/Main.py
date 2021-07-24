import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
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
    s = s_input()

    n = len(s)
    
    dp = [[0] * 9 for i in range(n+1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(9):
            dp[i+1][j] += dp[i][j]
            if s[i] == 'c' and j == 0:
                dp[i+1][j+1] += dp[i][j]
            if s[i] == 'h' and j == 1:
                dp[i+1][j+1] += dp[i][j]
            if s[i] == 'o' and j == 2:
                dp[i+1][j+1] += dp[i][j]
            if s[i] == 'k' and j == 3:
                dp[i+1][j+1] += dp[i][j]
            if s[i] == 'u' and j == 4:
                dp[i+1][j+1] += dp[i][j]
            if s[i] == 'd' and j == 5:
                dp[i+1][j+1] += dp[i][j]
            if s[i] == 'a' and j == 6:
                dp[i+1][j+1] += dp[i][j]
            if s[i] == 'i' and j == 7:
                dp[i+1][j+1] += dp[i][j]

    print(dp[n][8]%MOD)

if __name__ == '__main__':
    main()
