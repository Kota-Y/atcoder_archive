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

edges = [[] for _ in range(n)]

for i in range(1, n):
    b = i_input()
    edges[i].append(b-1)
    edges[b-1].append(i)

ans_list = [[] for _ in range(n)]

def dfs(current, parent, ans_list):
    if len(edges[current]) == 1 and parent != -1:
        ans_list[current].append(1)
        return 1
    else:
        for child in edges[current]:
            if child == parent:
                continue
            res = dfs(child, current, ans_list)
            ans_list[current].append(res)
        money = max(ans_list[current]) + min(ans_list[current]) + 1
        return money

res = dfs(0, -1, ans_list)

print(res)