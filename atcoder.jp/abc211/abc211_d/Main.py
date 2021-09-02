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

def create_graph(n: int, l: list) -> list:
    graph = [[] for _ in range(n)]
    for a, b in l:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    return graph

def bfs(graph: list, n: int, start: int, dist: list, cnt: list):
    q = deque([start])
    cnt[0] = 1
    dist[0] = 0
    while len(q) != 0:
        node = q.popleft()
        for leaf in graph[node]:
            if dist[leaf] == INF:
                dist[leaf] = dist[node] + 1
                cnt[leaf] = cnt[node]
                q.append(leaf)
            elif dist[leaf] == dist[node] + 1:
                cnt[leaf] += cnt[node]
                cnt[leaf] %= MOD

def main():
    n, m = i_map()
    num_list = i_row_list(m)
 
    graph = create_graph(n, num_list)
    
    dist = [INF] * n
    cnt = [0] * n
 
    bfs(graph, n, 0, dist, cnt)

    print(cnt[n-1])

if __name__ == '__main__':
    main()
