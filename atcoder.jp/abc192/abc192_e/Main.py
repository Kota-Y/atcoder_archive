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
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def dijkstra(start: int, node_num: int, edge: list) -> list:
    d = [float("inf")] * node_num
    d[start] = 0
    #スタートをキューに入れる
    q = [(0,start,1)]

    while len(q) != 0:
        #キューの先頭を取得
        ci, i, ki = heappop(q)
        if d[i] < ci:
            continue
        #キューの先頭から繋がっている頂点を探索
        for cj, j, kj in edge[i]:
            if d[j] > kj*ceil(d[i]/kj) + cj:
                d[j] = kj*ceil(d[i]/kj) + cj
                heappush(q, (d[j], j, kj))
                
    return d

def main():
    n, m, x, y = i_map()
    
    edges = [[] for _ in range(n)]

    for _ in range(m):
        a, b, t, k = i_map()
        edges[a-1].append((t, b-1, k))
        edges[b-1].append((t, a-1, k))

    tmp = dijkstra(x-1, n, edges)

    print(tmp[y-1] if tmp[y-1] != INF else -1)

if __name__ == '__main__':
    main()
