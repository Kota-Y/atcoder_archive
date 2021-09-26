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
MOD = 998244353
num_list = []
str_list = []

def main():
    n = i_input()
    num_list = i_list()

    mae = num_list[0]
    ushiro = num_list[1]
    d = defaultdict(int)
    d[(mae+ushiro)%10] += 1
    d[(mae*ushiro)%10] += 1

    for i in range(2, n):
        ushiro = num_list[i]
        tmp_d = defaultdict(int)
        for k, v in d.items():
            tmp_d[(k+ushiro)%10] += v
            tmp_d[(k*ushiro)%10] += v
        d = tmp_d.copy()

    for i in range(10):
        print(d[i]%MOD)

if __name__ == '__main__':
    main()
