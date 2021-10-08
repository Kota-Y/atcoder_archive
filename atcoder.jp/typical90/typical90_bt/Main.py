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

def dfs(i, j , cnt, h ,w, dist, str_list):
    if dist[i][j] != -1:
        if cnt - dist[i][j] >= 4:
            return cnt - dist[i][j]
        else:
            return -1

    num = -1
    dist[i][j] = cnt
    for dy, dx in ([1, 0], [-1, 0], [0, 1], [0, -1]):
        if not (0 <= dy + i <= h - 1 and 0 <= dx + j <= w - 1): continue
        if str_list[dy + i][dx + j] == "#": continue
        num = max(num, dfs(dy + i, dx + j, cnt + 1, h, w, dist, str_list))    
    dist[i][j] = -1

    return num


def main():
    h, w = i_map()
    str_list = s_row_list(h)

    ans = -1
    dist = [[-1]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if str_list[i][j] == '#':
                continue
            ans = max(ans, dfs(i, j, 0, h, w, dist, str_list))
    
    print(ans)

if __name__ == '__main__':
    main()
