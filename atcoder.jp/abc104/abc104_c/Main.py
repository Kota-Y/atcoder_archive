import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
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
def s_row_list(N): return [s_list() for _ in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []


def main():
    d, g = i_map()
    num_list = i_row_list(d)

    min_count = INF
    for bit in list(product([0,1], repeat=d)):
        tmp_score = 0
        tmp_count = 0
        max_i = -1
        for i in range(d):
            if bit[i] == 0:
                max_i = max(max_i, i)
                continue
            tmp_score += num_list[i][0] * 100 * (i+1) + num_list[i][1]
            tmp_count += num_list[i][0]
        if tmp_score < g:
            for _ in range(num_list[max_i][0]):
                tmp_score += 100 * (max_i+1)
                tmp_count += 1
                if tmp_score >= g:
                    break
        if tmp_score >= g:
            min_count = min(min_count, tmp_count)
        
    print(min_count)

if __name__ == '__main__':
    main()
