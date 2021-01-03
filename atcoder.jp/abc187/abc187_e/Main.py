import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
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
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

# TLEになるのでBFSでしてみる(while qのやつ)
# def dfs_depth(current, parent, depth):
#     depth_list[current] = depth
#     for child in edges[current]:
#         if child == parent:
#             continue
#         dfs_depth(child, current, depth+1)

# TLEになるのでBFSでしてみる(while qのやつ)
# def dfs(current, parent):
#     for child in edges[current]:
#         if child == parent:
#             continue
#         node_list[child] += node_list[current]
#         dfs(child, current)


n = i_input()
num_list = i_row_list(n-1)

edges = [[] for _ in range(n)]
for i in range(n-1):
    a, b = num_list[i][0], num_list[i][1]
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

depth_list = [-1] * n
depth_list[0] = 0
# dfs_depth(0, -1, 0)
q = [0]
while q:
    at = q.pop()
    for i in edges[at]:
        if depth_list[i] == -1:
            depth_list[i] = depth_list[at] + 1
            q.append(i)

node_list = [0] * n
q = i_input()
for _ in range(q):
    t, e, x = i_map()
    a, b = num_list[e-1]
    a, b = a-1, b-1
    if depth_list[a] > depth_list[b]:
        a, b = b, a
        t ^= 3
    if t == 1:
        node_list[0] += x
        node_list[b] -= x 
    elif t == 2:
        node_list[b] += x

# dfs(0, -1)

q = [0]
while q:
    at = q.pop()
    for i in edges[at]:
        if depth_list[at] < depth_list[i]:
            node_list[i] += node_list[at]
            q.append(i)

for node in node_list:
    print(node)

