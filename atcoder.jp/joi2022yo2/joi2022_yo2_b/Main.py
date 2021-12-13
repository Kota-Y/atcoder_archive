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
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

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

def main():
    h, w = i_map()
    str_list = s_row_list(h)
    
    edges = [[] for _ in range(h*w)]

    for i in range(h):
        for j in range(w):
            for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                ni = i + dx
                nj = j + dy
                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    continue
                if str_list[ni][nj] == str_list[i][j]:
                    continue
                edges[i*w+j].append((1, ni*w+nj))

    res = dijkstra(0, h*w, edges)

    print(res[h*w-1] if res[h*w-1] != INF else -1)

if __name__ == '__main__':
    main()


