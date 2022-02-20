from calendar import c
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

n = i_input()
edge_list = i_row_list(n-1)

edges = [[] for _ in range(n)]
for a, b in edge_list:
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

ans_list = [0] * n

def dfs(current, parent, co):
    if len(edges[current]) == 1 and parent != -1:
        ans_list[current] = [co, co]
        co += 1

        return co
    else:
        ans_list[current] = [co, -1]
        for child in edges[current]:
            if child == parent:
                continue
            co = dfs(child, current, co)
        tmp_min_co = ans_list[current][0]
        ans_list[current] = [tmp_min_co, co-1]

        return co

tmpp = dfs(0, -1, 1)

# print(edges)
# print(ans_list)

for l, r in ans_list:
    print(l, r)
