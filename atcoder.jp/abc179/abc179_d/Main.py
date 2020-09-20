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
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
# MOD = 10 ** 9 + 7
MOD = 998244353
num_list = []
str_list = []

def main():
    n, k = i_map()
    num_list = i_row_list(k)

    dp = [0] * (n+1)
    dp_sum = [0] * (n+1)
    dp[1] = 1
    dp_sum[1] = 1

    for i in range(2, n+1):
        for j in range(k):
            li = i - num_list[j][1]
            ri = i - num_list[j][0]
            if ri < 0:
                continue
            li = max(li, 0)
            dp[i] += dp_sum[ri] - dp_sum[li-1]
            dp[i] %= MOD
        dp_sum[i] = dp_sum[i-1] + dp[i]
    
    print(dp[n]%MOD)

if __name__ == '__main__':
    main()
