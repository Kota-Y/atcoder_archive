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

def bfs(si, sj, str_list, dist, h, w):
    q = deque([[si, sj]])
    dist[si][sj] = 0
    max_tmp = 0
    while len(q) != 0:
        i, j = q.popleft()
        for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
        #8方向ver for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]):
            ni = i + dx
            nj = j + dy
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if str_list[ni][nj] != '.':
                continue
            if dist[ni][nj] != INF:
                continue
            dist[ni][nj] = dist[i][j] + 1
            q.append([ni, nj])
            max_tmp = max(max_tmp, dist[ni][nj])
    return dist[h-1][w-1]

def main():
    h, w = i_map()
    str_list = s_row_list(h)

    count = 0
    for i in range(h):
        for j in range(w):
            if str_list[i][j] == '#':
                count += 1

    dist = [[INF] * w for i in range(h)]
    a = bfs(0, 0, str_list, dist, h, w)

    if a == INF:
        print(-1)
    else:
        print(h*w-a-count-1)

if __name__ == '__main__':
    main()
