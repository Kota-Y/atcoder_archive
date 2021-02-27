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
    s = s_input()
    t = s_input()

    nokori_card = n * 9 - 8
    pattern_num = nokori_card * (nokori_card-1)

    st = s + t
    st_co = Counter(st)

    ans = 0
    ans_list = []
    for i in range(1, 10):
        tmp_s = s.replace('#', str(i))
        s_co = Counter(tmp_s)

        for k in range(1, 10):
            tmp_t = t.replace('#', str(k))
            t_co = Counter(tmp_t)
            s_sum = 0
            t_sum = 0
        
            for j in range(1, 10):
                s_sum += j * pow(10, s_co[str(j)])
                t_sum += j * pow(10, t_co[str(j)])
            if s_sum > t_sum:
                ans_list.append([i, k])

    bunshi = 0
    for i, j in ans_list:
        tmp_i = n - st_co[str(i)]
        if tmp_i == 0:
            continue
        tmp_j = n - st_co[str(j)]
        if tmp_j == 0:
                continue
        if i != j:
            bunshi += tmp_i * tmp_j
        else:
            bunshi += tmp_i * (tmp_j-1)

    # print(bunshi, pattern_num)
    print(bunshi/pattern_num)

if __name__ == '__main__':
    main()
