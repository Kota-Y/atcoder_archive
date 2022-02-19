import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import floor, sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
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
def ceil(a, b): return (a + b - 1) // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    x1, y1, x2, y2 = i_map()
    
    ans1 = [
        [x1+1, y1+2],
        [x1+1, y1-2],
        [x1-1, y1+2],
        [x1-1, y1-2],
        [x1+2, y1+1],
        [x1+2, y1-1],
        [x1-2, y1+1],
        [x1-2, y1-1],
    ]

    ans2 = [
        [x2+1, y2+2],
        [x2+1, y2-2],
        [x2-1, y2+2],
        [x2-1, y2-2],
        [x2+2, y2+1],
        [x2+2, y2-1],
        [x2-2, y2+1],
        [x2-2, y2-1],
    ]

    for ans in ans1:
        if ans in ans2:
            print('Yes')
            exit()

    print('No')

if __name__ == '__main__':
    main()
