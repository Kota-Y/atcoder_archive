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
    n, q = i_map()
    num_list = i_row_list(n)

    max_x = 0
    max_y = 0
    min_x = INF
    min_y = INF

    for x, y in num_list:
        max_x = max(max_x, x+y)
        max_y = max(max_y, x-y)
        min_x = min(min_x, x+y)
        min_y = min(min_y, x-y)

    for _ in range(q):
        q = i_input()
        z_x = num_list[q-1][0] + num_list[q-1][1]
        z_y = num_list[q-1][0] - num_list[q-1][1]
        print(max(abs(z_x-min_x), abs(z_y-min_y), abs(z_x-max_x), abs(z_y-max_y)))

if __name__ == '__main__':
    main()
