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
    sn = str(n)

    if len(sn) <= 3:
        print(0)
        exit()

    ans = 0

    if len(sn) >= 7:
        ans += 1 * (999999-999)
    else:
        ans += 1 * (n-999)
        print(ans)
        exit()

    if len(sn) >= 10:
        ans += 2 * (999999999-999999)
    else:
        ans += 2 * (n-999999)
        print(ans)
        exit()

    if len(sn) >= 13:
        ans += 3 * (999999999999-999999999)
    else:
        ans += 3 * (n-999999999)
        print(ans)
        exit()

    ans += 4 * (n-999999999999)

    if n == 10**15:
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
