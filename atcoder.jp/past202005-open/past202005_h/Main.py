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
    n, l = i_map()
    num_list = i_list()
    t1, t2, t3 = i_map()

    hurdle = [0] * l
    for i in range(n):
        hurdle[num_list[i]] = 1

    dp = [INF] * (l+10)

    dp[0] = 0

    for i in range(l):
        add_cost = t3 if hurdle[i] else 0
        dp[i+1] = min(dp[i+1], dp[i] + t1 + add_cost)
        dp[i+2] = min(dp[i+2], dp[i] + t1 + t2 + add_cost)
        dp[i+4] = min(dp[i+4], dp[i] + t1 + t2*3 + add_cost)

        if i + 1 == l:
            dp[l] = min(dp[l], dp[i] + t1 // 2 + t2 // 2 + add_cost)
        if i + 2 == l:
            dp[l] = min(dp[l], dp[i] + t1 // 2 + t2 // 2 + t2 + add_cost)
        if i + 3 == l:
            dp[l] = min(dp[l], dp[i] + t1 // 2 + t2 // 2 + t2 *2 + add_cost)

    # print(dp)
    print(dp[l])

if __name__ == '__main__':
    main()
