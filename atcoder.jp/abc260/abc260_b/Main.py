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
    n, x, y, z = i_map()
    a_list = i_list()
    b_list = i_list()

    a_l = []
    for i, a in enumerate(a_list):
        a_l.append([a, i])
    a_l = sorted(a_l, key=lambda x:(-x[0], x[1]))

    b_l = []
    for i, b in enumerate(b_list):
        b_l.append([b, i])
    b_l = sorted(b_l, key=lambda x:(-x[0], x[1]))

    ab_l = []
    for i in range(n):
        ab_l.append([a_list[i]+b_list[i], i])
    ab_l = sorted(ab_l, key=lambda x:(-x[0], x[1]))

    ans_set = set()
    for _, i in a_l[:x]:
        ans_set.add(i)

    co = 0
    for _, i in b_l:
        if co >= y:
            break
        if i in ans_set:
            continue
        ans_set.add(i)
        co += 1

    co = 0
    for _, i in ab_l:
        if co >= z:
            break
        if i in ans_set:
            continue
        ans_set.add(i)
        co += 1

    ans_l = list(ans_set)
    ans_l.sort()
    for ans in ans_l:
        print(ans+1)

if __name__ == '__main__':
    main()
