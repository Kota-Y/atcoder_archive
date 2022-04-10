import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
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
def floor(a, b): return a // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    n = i_input()

    s1 = [1]
    s2 = [*s1, 2, *s1]
    s3 = [*s2, 3, *s2]
    s4 = [*s3, 4, *s3]
    s5 = [*s4, 5, *s4]
    s6 = [*s5, 6, *s5]
    s7 = [*s6, 7, *s6]
    s8 = [*s7, 8, *s7]
    s9 = [*s8, 9, *s8]
    s10 = [*s9, 10, *s9]
    s11 = [*s10, 11, *s10]
    s12 = [*s11, 12, *s11]
    s13 = [*s12, 13, *s12]
    s14 = [*s13, 14, *s13]
    s15 = [*s14, 15, *s14]
    s16 = [*s15, 16, *s15]

    ans = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16]
    print(*ans[n-1])

if __name__ == '__main__':
    main()
