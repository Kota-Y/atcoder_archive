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

n, q = i_map()
x_list = i_list()
edge_list = i_row_list(n-1)
query_list = i_row_list(q)

edges = [[] for _ in range(n)]
for a, b in edge_list:
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

ans_list = [[] for _ in range(n)]

def dfs(current, parent, edges, ans_list):
    tmp = [x_list[current]]
    for child in edges[current]:
        if child == parent:
            continue
        res = dfs(child, current, edges, ans_list)
        for i in res:
            tmp.append(i)

    tmp.sort(reverse=True)
    tmp = tmp[:21]
    # print(current, tmp)
    ans_list[current].append(tmp)
    return tmp

dfs(0, -1, edges, ans_list)

# print(ans_list)

for v, k in query_list:
    print(ans_list[v-1][0][k-1])
