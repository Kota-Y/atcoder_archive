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
    n = i_input()
    num_list = i_row_list(n)

    dp = [[1 << 25] * n for _ in range(1 << n)]
    dp[0][0] = 0

    for s in range(1 << n):
        for i in range(n):
            xi, yi, zi = num_list[i][0], num_list[i][1], num_list[i][2]
            if (1 << i) & s:
                for j in range(n):
                    xj, yj, zj = num_list[j][0], num_list[j][1], num_list[j][2]
                    cost = abs(xi - xj) + abs(yi - yj) + max(0, zj - zi)
                    dp[s][i] = min(dp[s][i], dp[s - (1 << i)][j] + cost)

    print(dp[(1 << n) - 1][0])

if __name__ == '__main__':
    main()
