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

n, q = i_map()

edges = [[] for _ in range(n)]
for i in range(n-1):
    a, b = i_map()
    edges[a-1].append((1, b-1))
    edges[b-1].append((1, a-1))

def dijkstra(start: int, node_num: int, edge: list) -> list:
    d = [float("inf")] * node_num
    d[start] = 0
    #スタートをキューに入れる
    q = [(0,start)]

    while len(q) != 0:
        #キューの先頭を取得
        ci, i = heappop(q)
        if d[i] < ci:
            continue
        #キューの先頭から繋がっている頂点を探索
        for cj, j in edge[i]:
            if d[j] > d[i] + cj:
                d[j] = d[i] + cj
                heappush(q, (d[j], j))
                
    return d

result = dijkstra(0, n, edges)

for _ in range(q):
    c, d = i_map()
    tmp = abs(result[c-1] - result[d-1])
    print('Town' if tmp % 2 == 0 else 'Road')

