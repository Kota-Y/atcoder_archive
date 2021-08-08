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

def dfs(current, parent, edges, visited):
    if visited[current] != 1:
        print(current+1)
        visited[current] = 1
    for child in edges[current]:
        if child == parent:
            continue
        dfs(child, current, edges, visited)
        print(current+1)

def main():
    n = i_input()

    edges_tmps = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = i_map()
        edges_tmps[a-1].append(b-1)
        edges_tmps[b-1].append(a-1)
    
    edges = []
    for edge in edges_tmps:
        edge.sort()
        edges.append(edge)

    visited = [0] * n

    dfs(0, -1, edges, visited)

if __name__ == '__main__':
    main()
