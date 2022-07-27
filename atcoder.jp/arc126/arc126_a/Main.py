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
    t = i_input()
    for _ in range(t):
        a, b, c = i_map()
        x1, x2, x3 = a, c, b // 2
        
        ans = 0

        min23 = min(x2, x3)
        ans += min23
        x2 -= min23
        x3 -= min23

        if x2 == 0:
            min113 = min(x1//2, x3)
            ans += min113
            x1 -= min113 * 2
            x3 -= min113
        else:
            min122 = min(x1, x2//2)
            ans += min122
            x1 -= min122
            x2 -= min122 * 2

            if x1 >= 3 and x2 >= 1:
                x1 -= 3
                x2 -= 1
                ans += 1

        ans += x1 // 5

        print(ans)

if __name__ == '__main__':
    main()
