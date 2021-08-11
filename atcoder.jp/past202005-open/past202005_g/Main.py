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

def bfs(si, sj, gx, gy, str_list, dist, h, w):
    q = deque([[si, sj]])
    dist[si][sj] = 0
    while len(q) != 0:
        i, j = q.popleft()
        for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1]):
            ni = i + dx
            nj = j + dy
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if str_list[ni][nj] == '#':
                continue
            if dist[ni][nj] != INF:
                continue
            dist[ni][nj] = dist[i][j] + 1
            q.append([ni, nj])
    # for i in range(h):
    #     print(dist[i])
    return dist[gx][gy] if dist[gx][gy] != INF else -1

def main():
    n, X, Y = i_map()
    num_list = []
    for _ in range(n):
        x, y = i_map()
        num_list.append([x, y])

    h = 403
    w = 403
    sx = h//2
    sy = w//2
    gx = h//2+X
    gy = h//2+Y

    str_list = [['.'] * w for _ in range(h)]

    for num in num_list:
        x, y = num[0], num[1]
        str_list[h//2+x][w//2+y] = '#'

    dist = [[INF] * w for _ in range(h)]

    print(bfs(sx, sy, gx, gy, str_list, dist, h, w))

if __name__ == '__main__':
    main()
