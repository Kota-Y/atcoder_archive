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

    for _ in range(n):
        t, l, r = i_map()
        l *= 10
        r *= 10
        if t == 1:
            l = l
            r = r
        if t == 2:
            l = l
            r = r - 1
        if t == 3:
            l = l + 1
            r = r
        if t == 4:
            l = l + 1
            r = r - 1
        num_list.append([l, r])

    num_list.sort()
    tmp_list = sorted(num_list, key=lambda x: x[1])

    ans = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if tmp_list[i][1] >= tmp_list[j][0]:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()
