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

def bfs(si, sj, str_list, dist, h, w, x):
    q = deque([[si, sj]])
    dist[si][sj] = 0
    while len(q) != 0:
        i, j = q.popleft()
        for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            ni = i + dx
            nj = j + dy
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if str_list[ni][nj] == '#':
                if dist[ni][nj] > dist[i][j] + x:
                    dist[ni][nj] = dist[i][j] + x
                    q.append([ni, nj])
            else:
                if dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append([ni, nj])
    return dist

def main():
    h, w, t = i_map()
    str_list = s_row_list(h)
    
    for i in range(h):
        for j in range(w):
            if str_list[i][j] == 'S':
                si, sj = i, j
            if str_list[i][j] == 'G':
                gi, gj = i, j

    low = 0
    higt = t
    while abs(higt-low) > 1:
        x = (low+higt) // 2
        dist = [[INF] * w for i in range(h)]
        bfs_result = bfs(si, sj, str_list, dist, h, w, x)
        time = bfs_result[gi][gj]
        if time <= t:
            low = x
        else:
            higt = x

    print(low)

if __name__ == '__main__':
    main()
