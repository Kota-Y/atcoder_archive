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

def main():
    h, w, n, m = i_map()
    grid_list = [[-1] * w for i in range(h)]
    for _ in range(n):
        i, j = i_map()
        grid_list[i-1][j-1] = 1 
    for _ in range(m):
        i, j = i_map()
        grid_list[i-1][j-1] = 0

    # 1: 電球
    # 0: ブロック
    # 2: 光が届いている(not電球)

    for i in range(h):
        for j in range(w):
            if grid_list[i][j] != 1:
                continue
            for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                ni = i + dx
                nj = j + dy
                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    continue
                if grid_list[ni][nj] == 0 or grid_list[ni][nj] == 1:
                    continue
                grid_list[ni][nj] = 2
                while True:
                    ni += dx
                    nj += dy
                    if ni < 0 or ni >= h or nj < 0 or nj >= w:
                        break
                    if grid_list[ni][nj] == 0 or grid_list[ni][nj] == 1:
                        break
                    grid_list[ni][nj] = 2

    count = 0
    for i in range(h):
        for j in range(w):
            if grid_list[i][j] == 1 or grid_list[i][j] == 2:
                count += 1

    print(count)

if __name__ == '__main__':
    main()
