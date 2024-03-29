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

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass


def main():
    n, l = i_map()
    k = i_input()
    num_list = i_list()
    
    ok = -1
    ng = l + 1
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        tmp = 0
        cat = 0
        cat_count = 0
        for i in range(n):
            tmp = num_list[i] - cat
            if tmp >= mid and l - (cat + tmp) >= mid:
                cat += tmp
                tmp = 0
                cat_count += 1
                # print(cat,cat_count,mid,i)
        # print(ok,ng,mid,cat_count)
        if cat_count >=k:
            ok = mid
        else:
            ng = mid

    print(ok)

if __name__ == '__main__':
    main()
