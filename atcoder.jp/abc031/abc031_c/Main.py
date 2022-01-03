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
from array import array
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
    num_list = i_list()
    
    ans_max = -INF

    for left in range(n):
        t_score = -INF
        a_score = -INF
        for right in range(n):
            if left == right:
                continue
            tmp_t_score = 0
            tmp_a_score = 0
            l = min(left, right)
            r = max(left, right)
            for co, i in enumerate(range(l, r+1)):
                if co % 2 == 0:
                    tmp_t_score += num_list[i]
                else:
                    tmp_a_score += num_list[i]
            if a_score < tmp_a_score:
                t_score = tmp_t_score
                a_score = tmp_a_score
                # print(left, right, t_score, a_score, ans_max)

        ans_max = max(ans_max, t_score)

    print(ans_max)

if __name__ == '__main__':
    main()
