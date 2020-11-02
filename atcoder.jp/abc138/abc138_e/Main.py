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
    S = s_input()
    T = s_input()

    s_co = Counter(S)
    for t in T:
        if t not in s_co.keys():
            print(-1)
            exit()

    index_list = {}
    for i, s in enumerate(S*2):
        if s not in index_list:
            index_list[s] = []
        index_list[s].append(i)

    ans = 0
    s_len = len(S)

    for t in T:
        r = ans % s_len
        p = bisect_left(index_list[t], r)
        n = ans // s_len
        ans = s_len * n + index_list[t][p] + 1

    print(ans)

if __name__ == '__main__':
    main()
