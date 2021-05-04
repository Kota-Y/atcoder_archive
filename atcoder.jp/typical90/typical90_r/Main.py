import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, sin, cos, radians, degrees, atan2
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
    t = i_input()
    l, x, y = i_map()
    q = i_input()

    for _ in range(q):
        e = i_input()

        theta = e / t * 360

        e8_x = 0
        e8_y = -l / 2 * sin(radians(theta))
        e8_z = l / 2  - l / 2 * cos(radians(theta))
        
        dist = sqrt((e8_x - x) ** 2 + (e8_y - y) ** 2)
        ans = degrees(atan2(e8_z, dist))
        print(ans)

if __name__ == '__main__':
    main()
