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
    n, m, q = i_map()
    num_list = i_row_list(n)
    x_list = i_list()

    num_list = sorted(num_list, key=lambda x: x[0])
    num_list = sorted(num_list, key=lambda x: -x[1])

    for _ in range(q):
        l, r = i_map()
        ans = 0
        box_list = []
        if r - l + 1 == m:
            print(ans)
            continue
        for i in range(m):
            if i+1 < l or r < i+1: 
                box_list.append(x_list[i])
        box_list.sort()
        for w, v in num_list:
            insert_index = bisect_left(box_list, w)
            if len(box_list) == insert_index:
                continue
            ans += v
            box_list.pop(insert_index)
            if len(box_list) == 0:
                break
        print(ans)

if __name__ == '__main__':
    main()
