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
    y = i_input()
    m = i_input()
    d = i_input()
    
    if m == 1 or m == 2:
        m += 12
        y -= 1

    ans1 = 365 * y + floor(y/4) - floor(y/100) + floor(y/400) + floor(306 * (m + 1) / 10) + d - 429

    y2 = 2014
    m2 = 5
    d2 = 17
    ans2 = 365 * y2 + floor(y2/4) - floor(y2/100) + floor(y2/400) + floor(306 * (m2 + 1) / 10) + d2 - 429

    print(ans2-ans1)

if __name__ == '__main__':
    main()
